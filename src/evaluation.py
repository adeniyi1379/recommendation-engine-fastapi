from surprise import accuracy


def evaluate_model(model, testset):

    predictions = model.test(testset)

    rmse = accuracy.rmse(predictions, verbose=False)

    return rmse
