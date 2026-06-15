from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.data_loader import load_movies


class EmbeddingService:

    def __init__(self):

        self.movies = load_movies()

        summaries = []

        for movie in self.movies:
            summaries.append(
                movie["summary"]
            )

        self.vectorizer = (
            TfidfVectorizer()
        )

        self.movie_vectors = (
            self.vectorizer.fit_transform(
                summaries
            )
        )

    def find_similar_movies(
        self,
        user_story
    ):

        user_vector = (
            self.vectorizer.transform(
                [user_story]
            )
        )

        similarity_scores = (
            cosine_similarity(
                user_vector,
                self.movie_vectors
            )[0]
        )

        results = []

        for index, score in enumerate(
            similarity_scores
        ):

            results.append({

                "title":
                    self.movies[index]["title"],

                "genre":
                    self.movies[index]["genre"],

                "similarity":
                    float(score)

            })

        results = sorted(
            results,
            key=lambda x: x["similarity"],
            reverse=True
        )

        return results