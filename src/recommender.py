import pandas as pd


def get_top_n_recommendations(user_id, model, ratings, movies, n=10):

    rated_movies = set(ratings[ratings["userId"] == user_id]["movieId"])

    all_movies = set(movies["movieId"])

    unseen_movies = all_movies - rated_movies

    predictions = []

    for movie_id in unseen_movies:

        pred = model.predict(uid=user_id, iid=movie_id)

        predictions.append((movie_id, pred.est))

    predictions = sorted(predictions, key=lambda x: x[1], reverse=True)

    top_n = predictions[:n]

    top_n = pd.DataFrame(top_n, columns=["movieId", "predicted_rating"])

    top_n = top_n.merge(movies, on="movieId")

    return top_n
