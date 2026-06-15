

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.data_loader import (
    load_movies
)


class ScriptAnalysisService:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.movies = load_movies()

    def analyze_script(
        self,
        script_text
    ):

        similar_movies = (
            self.embedding_service
            .find_similar_movies(
                script_text
            )
        )

        best_match = (
            similar_movies[0]
        )

        top_matches = []

        for movie in similar_movies[:3]:

            top_matches.append({

                "title":
                    movie["title"],

                "genre":
                    movie["genre"],

                "similarity":
                    round(
                        movie["similarity"],
                        4
                    )
            })

        result = {

            "most_similar_movie":
                best_match["title"],

            "genre":
                best_match["genre"],

            "similarity_score":
                round(
                    best_match["similarity"],
                    4
                ),

            "top_matches":
                top_matches
        }

        return result