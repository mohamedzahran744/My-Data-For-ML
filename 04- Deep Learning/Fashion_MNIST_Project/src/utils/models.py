from pydantic import BaseModel


class PredictionResponse(BaseModel):
    class_index: int
    class_name: str
    confidence: float