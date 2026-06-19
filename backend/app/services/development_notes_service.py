class DevelopmentNotesService:

    def generate_notes(
        self,
        scorecard,
        dna
    ):

        notes = {}

        if scorecard["character_depth"] < 80:
            notes["character"] = (
                "The protagonist's emotional depth could be expanded to create a stronger audience connection."
            )
        else:
            notes["character"] = (
                "Character development is strong and supports the narrative effectively."
            )

        if scorecard["emotional_impact"] < 80:
            notes["theme"] = (
                "The story's emotional themes could be reinforced through stronger personal stakes."
            )
        else:
            notes["theme"] = (
                "Themes are communicated clearly throughout the narrative."
            )

        if dna["pace"][0][0] == "Slow Burn":
            notes["structure"] = (
                "The middle section may benefit from additional turning points to maintain momentum."
            )
        else:
            notes["structure"] = (
                "Narrative pacing effectively builds tension toward the climax."
            )

        if dna["ending"][0][0] in [
            "Victory Climax",
            "Emotional Resolution"
        ]:
            notes["ending"] = (
                "The ending provides satisfying resolution but could further elevate emotional payoff."
            )
        else:
            notes["ending"] = (
                "The ending offers an unconventional resolution that supports the story's themes."
            )

        return notes