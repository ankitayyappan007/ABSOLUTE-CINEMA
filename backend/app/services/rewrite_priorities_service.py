class RewritePrioritiesService:

    def generate_priorities(
        self,
        scorecard,
        dna
    ):

        priorities = []

        if scorecard[
            "character_depth"
        ] < 80:

            priorities.append(
                "Strengthen protagonist depth and emotional complexity."
            )

        if scorecard[
            "emotional_impact"
        ] < 80:

            priorities.append(
                "Increase emotional stakes before the climax."
            )

        if dna["conflict"][0][0] == "Internal":

            priorities.append(
                "Externalize conflict to create stronger dramatic tension."
            )

        if dna["pace"][0][0] == "Slow Burn":

            priorities.append(
                "Improve pacing during the middle act."
            )

        if scorecard[
            "originality"
        ] < 75:

            priorities.append(
                "Introduce more distinctive narrative elements."
            )

        if len(priorities) == 0:

            priorities.append(
                "Story is well balanced. Focus on polish and execution."
            )

        return priorities[:3]