import json
from bayes_opt import BayesianOptimization
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import ModelMetadata
from .serializers import ModelMetadataSerializer
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from .model_pipeline import (
    rf_bo_classifier, optimize_rf_regressor, save_model, load_model, evaluate_model, predict_crop,
    X_train, X_test, y_train, y_test
)
from sklearn.ensemble import RandomForestClassifier
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@login_required
def train_classifier(request):
    pbounds_classifier = {
        'n_estimators': (50, 200),
        'max_depth': (5, 20),
        'min_samples_split': (2, 10),
        'min_samples_leaf': (1, 5),
        'max_features': (0.1, 0.999)
    }
    optimizer_classifier = BayesianOptimization(f=rf_bo_classifier, pbounds=pbounds_classifier, random_state=42, verbose=2)
    optimizer_classifier.maximize(init_points=5, n_iter=10)
    best_params_classifier = optimizer_classifier.max['params']
    best_rf_model_classifier = RandomForestClassifier(
        n_estimators=int(best_params_classifier['n_estimators']),
        max_depth=int(best_params_classifier['max_depth']),
        min_samples_split=int(best_params_classifier['min_samples_split']),
        min_samples_leaf=int(best_params_classifier['min_samples_leaf']),
        max_features=best_params_classifier['max_features'],
        random_state=42
    )
    best_rf_model_classifier.fit(X_train, y_train)
    y_pred_classifier = best_rf_model_classifier.predict(X_test)
    metrics_classifier = {
        'accuracy': accuracy_score(y_test, y_pred_classifier),
        'f1_score': f1_score(y_test, y_pred_classifier, average='weighted', zero_division=1),
        'precision': precision_score(y_test, y_pred_classifier, average='weighted', zero_division=1),
        'recall': recall_score(y_test, y_pred_classifier, average='weighted', zero_division=1)
    }
    save_model(best_rf_model_classifier)
    metadata = ModelMetadata(
        model_type='Classifier',
        accuracy=metrics_classifier['accuracy'],
        f1_score=metrics_classifier['f1_score'],
        precision=metrics_classifier['precision'],
        recall=metrics_classifier['recall'],
        user=request.user
    )
    if metadata.is_valid():
        metadata.save()
        return JsonResponse(metrics_classifier)
    else:
        return JsonResponse(metadata.errors, status=400)


@api_view(['POST'])
@login_required
def train_regressor(request):
    result = optimize_rf_regressor(X_train, y_train, X_test, y_test)
    best_model = result['best_model']
    score = result['score']   
    metadata = ModelMetadata(
        model_type='Regressor',
        regressor_score=score,
        user=request.user
    )
    metadata.save()
    save_model(best_model)
    return JsonResponse({'score': score})


@api_view(['GET'])
@login_required
def evaluate(request):
    model = load_model()
    if model:
        metrics = evaluate_model(model, X_test, y_test)
        return JsonResponse(metrics)
    return JsonResponse({'error': 'Model not found'}, status=404)


@api_view(['POST'])
@login_required
def predict(request):
    model = load_model()
    if not model:
        return JsonResponse({'error': 'Model not found'}, status=404)
    new_data = request.data
    if not new_data:
        return JsonResponse({'error': 'No data provided'}, status=400)
    try:
        data = [
            new_data['urea'],
            new_data['phosphorous'],
            new_data['potassium'],
            new_data['temperature'],
            new_data['humidity'],
            new_data['ph'],
            new_data['rainfall']
        ]       
    except KeyError as e:        
        return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': f'Invalid data format: {str(e)}'}, status=400)
    try:
        prediction = predict_crop(model, data)
        try:
            return JsonResponse({'predicted_yield': prediction},{'prediction_model':ModelMetadata})
        except Exception as e:
            error_message = str(e)
            if "unseen labels" in error_message:
                return "Error: Model encountered unseen labels during prediction."
            else:
                return f"Error: {error_message}"
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)   