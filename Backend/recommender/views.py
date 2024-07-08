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
    """
    Train a Random Forest classifier using Bayesian Optimization.

    This endpoint performs hyperparameter optimization using Bayesian Optimization
    to train a Random Forest classifier on a training dataset. It then evaluates
    the model on a test dataset and returns evaluation metrics.

    Example Request:
    {
        "X_train": [[1, 2, 3], [4, 5, 6], ...],
        "y_train": [0, 1, 0, ...],
        "X_test": [[7, 8, 9], [10, 11, 12], ...],
        "y_test": [1, 0, 1, ...]
    }

    Responses:
    - 200 OK: Successfully trained the classifier and returned evaluation metrics.
        {
            "accuracy": 0.85,
            "f1_score": 0.83,
            "precision": 0.88,
            "recall": 0.80
        }

    Notes:
    - This endpoint requires the user to be authenticated.
    - It uses Bayesian Optimization to find the best hyperparameters for the Random Forest classifier.
    - The trained model and evaluation metrics are saved in the database.
    """
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
    
    metadata.save()
    return JsonResponse(metrics_classifier)


@api_view(['POST'])
@login_required
def train_regressor(request):
    """
    Train a Random Forest regressor model and save the best model.

    This endpoint optimizes a Random Forest regressor using the provided training
    and testing datasets. The best model is saved, and its score is returned.

    Example request body (JSON):
    {
        "X_train": [...],  #  actual training data here
        "y_train": [...],  #  actual training labels here
        "X_test": [...],   # actual testing data here
        "y_test": [...]    #  actual testing labels here
    }

    Parameters:
    - request (HttpRequest): The HTTP request object containing the training and testing data.

    Responses:
    - 200 OK: The model was trained successfully, and the score is returned.
        {
            "score": 0.85  
        }

    Returns:
    JsonResponse: A JSON response containing the score of the trained model.
    """
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
    """
    Evaluate the model and return its performance metrics.

    This endpoint loads a pre-trained model, evaluates it on a test dataset,
    and returns the evaluation metrics.

    Example:
    GET /api/evaluate/

    Example Response (200 OK):
    {
        "accuracy": 0.95,
        "precision": 0.92,
        "recall": 0.93,
        "f1_score": 0.92
    }

    Example Response (404 Not Found):
    {
        "error": "Model not found"
    }

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: A JSON response containing the evaluation metrics for the Classifier Model or Score for a Regressor Model or an error message.
    """
    model = load_model()
    if model:
        metrics = evaluate_model(model, X_test, y_test)
        return JsonResponse(metrics)
    return JsonResponse({'error': 'Model not found'}, status=404)


@api_view(['POST'])
@login_required
def predict(request):
    """
    Predict the crop based on the provided agricultural data.

    This endpoint loads a pre-trained model, predicts the crop based on the provided
    agricultural data, and returns the predicted crop.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the agricultural data in JSON format.
    
    Example:
    ```
    {
        "urea": 46.0,
        "phosphorous": 22.0,
        "potassium": 15.0,
        "temperature": 27.5,
        "humidity": 82.0,
        "ph": 6.5,
        "rainfall": 200.0
    }
    ```

    Responses:
    - 200 OK: Successful prediction of the crop.
        {
            "predicted_crop": "Wheat"
        }
    - 400 Bad Request: Bad request due to missing or invalid data.
        {
            "error": "No data provided" / "Missing field: urea" / "Invalid data format: could not convert string to float"
        }
    - 404 Not Found: Model not found.
        {
            "error": "Model not found"
        }
    - 500 Internal Server Error: An unexpected error occurred.
        {
            "error": "An unexpected error occurred."
        }

    Returns:
    JsonResponse: A JSON response containing the predicted crop or an error message.
    """
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
            return JsonResponse({'predicted_crop': prediction})
        except Exception as e:
            error_message = str(e)
            if "unseen labels" in error_message:
                return "Error: Model encountered unseen labels during prediction."
            else:
                return f"Error: {error_message}"
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)   