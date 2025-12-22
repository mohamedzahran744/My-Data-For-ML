import pandas as pd
from .PatiantData import PatiantData  # Import patient data model/schema

def predict_new(data: PatiantData, preprocessor, model):
    """
    Make a prediction for a new patient's diagnosis based on input features.
    
    Args:
        data (PatiantData): Patient data object containing feature values
        preprocessor: Fitted preprocessor (scaler/imputer) for data transformation
        model: Trained classification model for making predictions
    
    Returns:
        dict: Dictionary containing diagnosis result and malignant probability
    """
    
    # Convert patient data object to pandas DataFrame
    # model_dump() extracts data as dictionary, wrapped in list for single-row DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Apply preprocessing transformations (imputation and scaling)
    # Uses the same transformations learned during training to ensure consistency
    x_processed = preprocessor.transform(df)

    # Make binary prediction (0: Benign, 1: Malignant)
    # predict() returns the class label
    y_predict = model.predict(x_processed)
    
    # Get prediction probabilities for both classes
    # predict_proba() returns [probability_benign, probability_malignant]
    y_prob = model.predict_proba(x_processed)

    # Convert numerical prediction to human-readable diagnosis
    # 1 = Malignant (cancerous), 0 = Benign (non-cancerous)
    result_name = "Malignant" if y_predict[0] == 1 else "Benign"

    # Return prediction results as dictionary
    # Includes diagnosis and confidence level (probability of malignancy)
    return {
        "Result": result_name,  # Diagnosis: "Benign" or "Malignant"
        "Malignant Probability": float(y_prob[0][1])  # Probability of being malignant (0-1)
    }