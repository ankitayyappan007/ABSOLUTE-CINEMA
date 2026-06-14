import json


def load_movies():

    with open("data/movies.json", "r", encoding="utf-8") as file:

        movies = json.load(file)

    return movies