import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib
import os

MODEL_PATH = 'recommender\models\ensemble_model.pkl'
DATA_PATH = 'recommender\data\Crop_recommendation.csv'

# Data preprocessing
def preprocess_data(data):
    scaler = StandardScaler()
    features = data[['urea', 'phosphorous', 'potassium', 'temperature', 'ph']]
    labels = data['crop_label']
    features_scaled = scaler.fit_transform(features)
    return train_test_split(features_scaled, labels, test_size=0.2, random_state=42)

# Model trainingfygt
def train_models(X_train, y_train):
    classifiers = {
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(probability=True),
        'Naive Bayes': GaussianNB()
    }
    for name, clf in classifiers.items():
        clf.fit(X_train, y_train)
    return classifiers

# Voting ensemble
def create_voting_classifier(classifiers, X_train, y_train):
    voting_clf = VotingClassifier(
        estimators=[(name, clf) for name, clf in classifiers.items()],
        voting='soft'
    )
    voting_clf.fit(X_train, y_train)
    return voting_clf

# Save the model
def save_model(model, model_path=MODEL_PATH):
    joblib.dump(model, model_path)

# Load the model
def load_model(model_path=MODEL_PATH):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

# Model evaluation
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }
    return metrics

# Prediction function
def predict_crop(model, new_data):
    return model.predict([new_data])

# Function to load dataset from CSV
def load_data(data_path=DATA_PATH):
    data = pd.read_csv(data_path)
    return data

# Example usage:
if __name__ == "__main__":
    # Load data
    data = load_data()

    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Train models
    classifiers = train_models(X_train, y_train)

    # Create voting classifier
    voting_clf = create_voting_classifier(classifiers, X_train, y_train)

    # Save the model
    save_model(voting_clf)

    # Load the model
    loaded_model = load_model()

    # Evaluate the model
    if loaded_model:
        evaluation_metrics = evaluate_model(loaded_model, X_test, y_test)
        print("Evaluation Metrics:")
        print(evaluation_metrics)

    # Example prediction
    new_data = np.array([0.5, 0.8, 0.6, 25.0, 6.5])  # Example new data for prediction
    predicted_crop = predict_crop(loaded_model, new_data)
    print("Predicted Crop:", predicted_crop)
