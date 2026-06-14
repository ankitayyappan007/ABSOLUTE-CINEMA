from app.services.dna_service import DNAService


class PriorityFusionService:

    def __init__(self):

        self.dna_service = DNAService()

    def fuse_with_priority(self, movie_weights):

        result = {}

        first_movie = next(iter(movie_weights))
        first_dna = self.dna_service.get_movie_dna(first_movie)

        dna_keys = first_dna.keys()

        for key in dna_keys:

            result[key] = []

        for movie, weight in movie_weights.items():

            dna = self.dna_service.get_movie_dna(movie)

            if dna:

                for key in dna_keys:

                    result[key].append(
                        (dna[key], weight)
                    )

        return result