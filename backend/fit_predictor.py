import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Function to load and prepare your dataset
def load_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    df = df[['matched_skills', 'missing_skills', 'title_match_score', 'fit_score']]
    return df

# Function to train the fit predictor model
def train_fit_predictor():
    # Load your training data
    data = load_data('./datasets/your_training_data.csv')  # Adjust the path as necessary

    # Prepare features and target variable
    X = data[['matched_skills', 'missing_skills', 'title_match_score']]
    y = data['fit_score']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestRegressor()

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Model Mean Squared Error: {mse}')

    # Save the model
    joblib.dump(model, 'fit_score_model.joblib')

# Function to load the trained model
def load_fit_model(filename='fit_score_model.joblib'):
    """Load the trained model from a file."""
    model = joblib.load(filename)
    return model
def predict_fit_score(model, matched_count, missing_count, title_match):
    features = np.array([[matched_count, missing_count, title_match]])
    return model.predict(features)[0]
