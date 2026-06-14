from app.services.data_loader import load_movies


class DNAService:

    def __init__(self):

        self.movies = load_movies()

    def get_movie_dna(self, title):

        for movie in self.movies:

            if movie["title"].lower() == title.lower():

                return movie["dna"]

        return None