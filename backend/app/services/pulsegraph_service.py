from app.services.data_loader import load_movies


class PulseGraphService:

    def __init__(self):

        self.movies = load_movies()

    def get_pulsegraph(self, movie_title):

        for movie in self.movies:

            if movie["title"].lower() == movie_title.lower():

                return movie["pulsegraph"]

        return None