# Movie Recommendation System

## Overview

This project implements a personalized movie recommendation system using the MovieLens dataset. The goal is to recommend movies to users based on historical rating patterns and collaborative filtering techniques.

The project explores both traditional recommendation algorithms and matrix factorization techniques before exposing the final recommendation model through a FastAPI REST API.

---

## Business Problem

Streaming platforms such as Netflix, Spotify, and YouTube rely heavily on recommendation systems to improve user engagement and content discovery.

This project demonstrates how recommendation systems can:

* Personalize content for individual users
* Predict user preferences for unseen items
* Improve content discovery
* Support decision-making using historical interaction data

---

## Dataset

### MovieLens Latest Small Dataset

Dataset Statistics:

| Metric  | Value   |
| ------- | ------- |
| Users   | 610     |
| Movies  | 9,724   |
| Ratings | 100,836 |

The dataset contains:

* User IDs
* Movie IDs
* Ratings
* Timestamps
* Movie metadata

---

## Recommendation Approaches Implemented

### 1. Popularity-Based Recommendation

Recommends the most frequently rated movies.

**Advantages**

* Simple
* Fast
* Useful for cold-start users

**Limitations**

* Not personalized

---

### 2. User-Based Collaborative Filtering

Recommendations are generated from users with similar rating behavior.

**Technique**

* User-Item Matrix
* Cosine Similarity

---

### 3. Item-Based Collaborative Filtering

Recommendations are generated from movies with similar rating patterns.

**Technique**

* Movie-User Matrix
* Cosine Similarity

---

### 4. Matrix Factorization (SVD)

The final recommendation model uses Singular Value Decomposition (SVD) from the Surprise library.

The model learns latent factors that capture hidden relationships between users and movies.

Examples of latent factors include:

* Action preference
* Thriller preference
* Romance preference
* Comedy preference

---

## Project Architecture

```text
MovieLens Dataset
        ↓
 Data Processing
        ↓
 User-Item Matrix
        ↓
   SVD Model
        ↓
 Model Evaluation
        ↓
 Save Model (.pkl)
        ↓
     FastAPI
        ↓
 Recommendation API
```

---

## Model Evaluation

### Metric

Root Mean Squared Error (RMSE)

### Result

RMSE = 0.8781

This indicates that predicted ratings are reasonably close to actual user ratings.

---

## API Development

The recommendation engine is deployed through FastAPI.
## Live Demo

API Documentation:

https://recommendation-system-api-sfsi.onrender.com/docs

Recommendation Endpoint:

https://recommendation-system-api-sfsi.onrender.com/recommend/1

### Endpoint

```http
GET /recommend/{user_id}
```

### Example

```http
GET /recommend/1
```

### Example Response

```json
[
  {
    "title": "Lawrence of Arabia (1962)",
    "predicted_rating": 4.36
  },
  {
    "title": "Rear Window (1954)",
    "predicted_rating": 4.34
  }
]
```

---

## Project Structure

```text
recommendation_system/
│
├── app/
│   ├── main.py
│   └── schemas.py
│
├── src/
│   ├── data_loader.py
│   ├── matrix_factorization.py
│   ├── recommender.py
│   ├── evaluation.py
│   └── model_utils.py
│
├── models/
│   └── svd_model.pkl
│
├── data/
│   └── ml-latest-small/
│
├── notebooks/
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Scikit-Surprise
* FastAPI
* Pydantic
* Git
* GitHub

---

## Key Skills Demonstrated

* Recommendation Systems
* Collaborative Filtering
* Matrix Factorization
* Machine Learning Evaluation
* API Development
* Software Engineering
* Model Persistence
* Git Version Control

---

## Future Improvements

* Music Recommendation System
* Implicit Feedback Recommendations
* Embedding-Based Recommendations
* Deep Learning Recommenders
* Cloud Deployment
* Real-Time Recommendations

---

## Author

**Adeniyi Aderonmu**

Mathematics Graduate | Data Analyst | Aspiring Quantitative Finance and Machine Learning Professional
