import os
import joblib
import numpy as np
import pandas as pd
from bayes_opt import BayesianOptimization
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

'''

apis dir for docker containerization(WORKDIR /apis) 
otherwise locally 
remove the apis/ in the path 
for MODEL_PATH & crop_data

'''
MODEL_PATH = r'apis\recommender\models\ensemble_model.pkl'

crop_data = pd.read_csv(r'apis\recommender\data\Crop_recommendation.csv')
X = crop_data.drop(columns=['crop_label'])
y = crop_data['crop_label']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

def rf_bo_classifier(n_estimators, max_depth, min_samples_split, min_samples_leaf, max_features):
    n_estimators = int(n_estimators)
    max_depth = int(max_depth)
    min_samples_split = int(min_samples_split)
    min_samples_leaf = int(min_samples_leaf)
    
    rf_model = RandomForestClassifier(n_estimators=n_estimators,
                                      max_depth=max_depth,
                                      min_samples_split=min_samples_split,
                                      min_samples_leaf=min_samples_leaf,
                                      max_features=max_features,
                                      random_state=42)
    
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=1)
    return f1

def rf_bo_regressor(n_estimators, max_depth, min_samples_split, max_features):
    n_estimators = int(n_estimators)
    max_depth = int(max_depth)
    min_samples_split = int(min_samples_split)

    rf_model = RandomForestRegressor(n_estimators=n_estimators,
                                      max_depth=max_depth,
                                      min_samples_split=min_samples_split,
                                      max_features=max_features,
                                      random_state=42)

    rf_model.fit(X_train, y_train)
    score = rf_model.score(X_test, y_test)
    return score

def optimize_rf_regressor(X_train, y_train, X_test, y_test):
    pbounds = {
        'n_estimators': (50, 200),
        'max_depth': (5, 20),
        'min_samples_split': (2, 10),
        'max_features': (0.1, 0.999)
    }
    
    optimizer = BayesianOptimization(f=rf_bo_regressor, pbounds=pbounds, random_state=42, verbose=2)
    optimizer.maximize(init_points=5, n_iter=10)
    
    best_params = optimizer.max['params']
    best_n_estimators = int(best_params['n_estimators'])
    best_max_depth = int(best_params['max_depth'])
    best_min_samples_split = int(best_params['min_samples_split'])
    best_max_features = best_params['max_features']
    
    best_rf_model_regressor = RandomForestRegressor(n_estimators=best_n_estimators,
                                          max_depth=best_max_depth,
                                          min_samples_split=best_min_samples_split,
                                          max_features=best_max_features,
                                          random_state=42)

    best_rf_model_regressor.fit(X_train, y_train)
    score = best_rf_model_regressor.score(X_test, y_test)
    return {'best_model': best_rf_model_regressor, 'score': score}

def save_model(model, model_path=MODEL_PATH):
    joblib.dump(model, model_path)

def load_model(model_path=MODEL_PATH):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def evaluate_model(model, X_test, y_test):
    if isinstance(model, RandomForestClassifier):
        y_pred = model.predict(X_test)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=1),
            'precision': precision_score(y_test, y_pred, average='weighted', zero_division=1),
            'recall': recall_score(y_test, y_pred, average='weighted', zero_division=1)
        }
        return metrics
    elif isinstance(model, RandomForestRegressor):
        score = model.score(X_test, y_test)
        return {'score': score}
    else:
        return None

def predict_crop(model, new_data):
    data = np.array([new_data])
    predicted_crop_encode = model.predict(data)
    predicted_crop_encoded = np.round(predicted_crop_encode).astype(int)
    predicted_crop = label_encoder.inverse_transform(predicted_crop_encoded)
    return predicted_crop[0] 