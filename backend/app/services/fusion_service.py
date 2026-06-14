from app.services.dna_service import DNAService


class FusionService:

    def __init__(self):

        self.dna_service = DNAService()

    def fuse_movies(self, movie_titles):

        fused_dna = {}

        dna_profiles = []

        for title in movie_titles:

            dna = self.dna_service.get_movie_dna(title)

            if dna:

                dna_profiles.append(dna)

        if not dna_profiles:

            return None

        dna_keys = dna_profiles[0].keys()

        for key in dna_keys:

            fused_dna[key] = []

            for dna in dna_profiles:

                fused_dna[key].append(dna[key])

        return fused_dna