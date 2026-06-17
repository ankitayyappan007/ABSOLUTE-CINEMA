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

        overall = scorecard["overall"]
        originality = scorecard["originality"]
        commercial = scorecard["commercial_appeal"]
        cinematic = scorecard["cinematic_potential"]

        if (
            overall >= 90
            and originality >= 85
            and commercial >= 85
            and cinematic >= 85
        ):
            recommendation = "STRONGLY RECOMMEND"

        elif (
            overall >= 80
            and originality >= 75
        ):
            recommendation = "RECOMMEND"

        elif overall >= 65:
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