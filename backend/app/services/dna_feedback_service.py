from app.services.dna_service import DNAService


class DNAFeedbackService:

    def __init__(self):

        self.dna_service = DNAService()

    def generate_dna_feedback(
        self,
        movie_title
    ):

        dna = (
            self.dna_service
            .get_movie_dna(
                movie_title
            )
        )

        if not dna:

            return "DNA not found."

        report = f"""

DNA ANALYSIS

Structure:
{dna["structure"]}

Tone:
{dna["tone"]}

Conflict:
{dna["conflict"]}

Ending:
{dna["ending"]}

Protagonist Arc:
{dna["protagonist_arc"]}

Observation:
This narrative is driven by a
{dna["tone"].lower()} tone,
an {dna["conflict"].lower()} conflict,
and a {dna["structure"].lower()} storytelling structure.

"""

        return report