class OriginalityReportService:

    def generate_report(
        self,
        weights,
        dna,
        scorecard
    ):

        tone = dna["tone"][0][0]

        conflict = dna["conflict"][0][0]

        structure = dna["structure"][0][0]

        originality_score = (
            scorecard["originality"]
        )

        description = (

            f"A {tone.lower()} story "

            f"with a {structure.lower()} "

            f"structure driven by "

            f"{conflict.lower()} conflict."
        )

        if originality_score >= 90:

            verdict = (
                "Highly Original"
            )

        elif originality_score >= 80:

            verdict = (
                "Strongly Distinctive"
            )

        elif originality_score >= 70:

            verdict = (
                "Moderately Original"
            )

        else:

            verdict = (
                "Familiar Concept"
            )

        return {

            "description":
                description,

            "verdict":
                verdict,

            "score":
                originality_score
        }