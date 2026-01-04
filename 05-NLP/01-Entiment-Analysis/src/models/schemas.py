from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    texts: List[str] = Field(
        ...,
        description="List of input texts to classify",
        min_length=1
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "texts": [
                    "This is a great product!",
                    "I hate this service",
                    "The product works as expected"
                ]
            }
        }
    }


class SentimentPrediction(BaseModel):
    text: str
    sentiment: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "This is a great product!",
                "sentiment": "Positive"
            }
        }
    }


class PredictionResponse(BaseModel):
    predictions: List[SentimentPrediction]

    model_config = {
        "json_schema_extra": {
            "example": {
                "predictions": [
                    {
                        "text": "This is a great product!",
                        "sentiment": "Positive"
                    },
                    {
                        "text": "I hate this service",
                        "sentiment": "Negative"
                    }
                ]
            }
        }
    }
