import pandas as pd 
from .CustomerData import CustomerData


def predict_new(data: CustomerData, preprocessor, model):

    # to DF 
    df = pd.DataFrame([data.model_dump()])

    # transform 
    x_processed = preprocessor.transform(df)

    # predict 
    y_predict = model.predict(x_processed)
    y_prob = model.predict_proba(x_processed)

    return {
        "Churn_prediction": bool(y_predict[0]),
        "Churn_probability": float(y_prob[0][1])
    }