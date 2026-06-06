from fastapi import FastAPI, HTTPException
from typing import List

from src.data_loader import load_data
from src.model_utils import save_model, load_model
from src.recommender import get_top_n_recommendations
from app.schemas import Recommendation
app = FastAPI()

ratings, movies = load_data("data")
model = load_model("models/svd_model.pkl")
@app.get("/")
def home():
    return {"message": "Welcome to the Movie Recommender API!"}


@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {
        "user_id": user_id,
        "message": f"Hello, user {user_id}"
        }
    
    
@app.get("/recommend/{user_id}", response_model=List[Recommendation])
def get_recommend(user_id:int):
    valid_user_ids = set(ratings["userId"])
    if user_id not in valid_user_ids:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        recommendations = get_top_n_recommendations(user_id, model, ratings, movies)
        
        return recommendations[["predicted_rating", "title"]].to_dict(orient="records")