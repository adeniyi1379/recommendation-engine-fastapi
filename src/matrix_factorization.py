from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise.model_selection import train_test_split


def train_svd_model(ratings, test_size=0.2, random_state=42):

    reader = Reader(rating_scale=(0.5, 5.0))

    data = Dataset.load_from_df(ratings[["userId", "movieId", "rating"]], reader)

    trainset, testset = train_test_split(
        data, test_size=test_size, random_state=random_state
    )

    model = SVD()

    model.fit(trainset)

    return model, testset
