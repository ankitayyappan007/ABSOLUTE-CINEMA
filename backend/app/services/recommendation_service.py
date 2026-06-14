class RecommendationService:

    def generate_feedback(
        self,
        dna
    ):

        strengths = []
        improvements = []

        tone = dna["tone"][0][0]
        conflict = dna["conflict"][0][0]
        ending = dna["ending"][0][0]
        protagonist = dna["protagonist_arc"][0][0]

        if (
            tone == "Psychological"
            and conflict == "Internal"
        ):

            strengths.extend([
                "Strong psychological depth",
                "Clear internal character struggle"
            ])

            improvements.extend([
                "Increase suspense between major reveals",
                "Make emotional stakes more visible"
            ])

        if (
            tone == "Emotional"
            and conflict == "Existential"
        ):

            strengths.extend([
                "Powerful emotional core",
                "Strong thematic depth"
            ])

            improvements.extend([
                "Clarify philosophical themes earlier",
                "Strengthen emotional payoff before the climax"
            ])

        if (
            tone == "Aggressive"
            and conflict == "External"
        ):

            strengths.extend([
                "High-energy storytelling",
                "Strong audience engagement potential"
            ])

            improvements.extend([
                "Give supporting characters more depth",
                "Create more tension before major victories"
            ])

        if ending == "Twist Ending":

            strengths.append(
                "Memorable ending potential"
            )

            improvements.append(
                "Plant more foreshadowing earlier"
            )

        if ending == "Emotional Resolution":

            strengths.append(
                "Strong emotional closure"
            )

            improvements.append(
                "Increase emotional buildup in Act 2"
            )

        if ending == "Victory Climax":

            strengths.append(
                "Satisfying audience payoff"
            )

            improvements.append(
                "Raise stakes before the final confrontation"
            )

        if protagonist == "Self Sacrifice":

            strengths.append(
                "Compelling heroic arc"
            )

        if protagonist == "Mental Collapse":

            strengths.append(
                "Complex character trajectory"
            )

        if protagonist == "Power Ascension":

            strengths.append(
                "Strong transformation arc"
            )

        if not strengths:

            strengths.append(
                "Strong narrative foundation"
            )

        if not improvements:

            improvements.append(
                "Increase emotional engagement"
            )

        return {
            "strengths": strengths,
            "improvements": improvements
        }