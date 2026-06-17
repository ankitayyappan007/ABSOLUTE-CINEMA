class ConsultantCoverageService:

    def generate_coverage(
        self,
        closest_match,
        scorecard,
        theme_analysis
    ):

        premise = (
            f"This story most closely resembles "
            f"{closest_match} and explores themes of "
            f"{', '.join(theme_analysis['themes'])}."
        )

        strengths = []

        if scorecard["originality"] >= 80:
            strengths.append(
                "Strong originality"
            )

        if scorecard["commercial_appeal"] >= 80:
            strengths.append(
                "Strong commercial appeal"
            )

        if scorecard["cinematic_potential"] >= 80:
            strengths.append(
                "High cinematic potential"
            )

        concerns = []

        if scorecard["emotional_impact"] < 80:
            concerns.append(
                "Emotional impact can be improved"
            )

        if scorecard["character_depth"] < 80:
            concerns.append(
                "Character depth requires development"
            )

        overall = scorecard["overall"]

        if overall >= 85:
            recommendation = "RECOMMEND"

        elif overall >= 70:
            recommendation = "CONSIDER"

        else:
            recommendation = "PASS"

        return {

            "premise":
                premise,

            "strengths":
                strengths,

            "concerns":
                concerns,

            "recommendation":
                recommendation
        }