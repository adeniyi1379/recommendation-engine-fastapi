import pandas as pd


def load_data(data_path):
    # Load movielen data
    ratings = pd.read_csv(f"{data_path}/ratings.csv")
    movies = pd.read_csv(f"{data_path}/movies.csv")

    return ratings, movies
