# Movie Recommendation System

## Overview

This project implements a movie recommendation system using the MovieLens dataset.

The project explores multiple recommendation approaches, including:

* Popularity-Based Recommendation
* User-Based Collaborative Filtering
* Item-Based Collaborative Filtering
* Matrix Factorization using Singular Value Decomposition (SVD)

The final model is deployed through a FastAPI application that serves personalized movie recommendations.

## Features

* Personalized movie recommendations
* Matrix Factorization (SVD)
* Model persistence using Pickle
* REST API with FastAPI
* Automatic API documentation
* Error handling for invalid users

## Dataset

MovieLens Latest Small Dataset

* 610 users
* 9,724 movies
* 100,836 ratings

## Model Performance

RMSE: 0.8781

## API Endpoint

Get recommendations for a user:

/recommend/{user_id}

Example:

/recommend/1

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Scikit-Surprise
* FastAPI
* Pydantic

## Future Improvements

* Music Recommendation System
* Embedding-Based Recommendations
* Deep Learning Recommenders
* Cloud Deployment
