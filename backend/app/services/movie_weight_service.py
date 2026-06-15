class MovieWeightService:

    def generate_weights(
        self,
        top_matches
    ):

        total_similarity = sum(
            movie["similarity"]
            for movie in top_matches
        )

        if total_similarity == 0:

            return {
                movie["title"]: 0
                for movie in top_matches
            }

        weights = {}

        for movie in top_matches:

            weight = round(
                (
                    movie["similarity"]
                    / total_similarity
                ) * 100
            )

            weights[
                movie["title"]
            ] = weight

        return weights