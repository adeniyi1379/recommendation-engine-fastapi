from pydantic import BaseModel

class Recommendation(BaseModel):
    title: str
    predicted_rating: float