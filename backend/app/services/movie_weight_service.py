class MovieWeightService:

    def generate_weights(
        self,
        top_matches
    ):

        total_similarity = sum(

            movie["similarity"]

            for movie in top_matches
        )

        weights = {}

        for movie in top_matches:

            percentage = round(

                (
                    movie["similarity"]
                    / total_similarity
                ) * 100

            )

            weights[
                movie["title"]
            ] = percentage

        return weights