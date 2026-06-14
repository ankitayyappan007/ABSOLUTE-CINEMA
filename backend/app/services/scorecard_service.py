class ScorecardService:

    def generate_scorecard(
        self,
        dna
    ):

        tone = dna["tone"][0][0]
        conflict = dna["conflict"][0][0]
        ending = dna["ending"][0][0]

        originality = 75
        emotional = 75
        character = 75
        commercial = 75
        cinematic = 75

        if tone == "Psychological":
            originality += 10
            character += 10

        if tone == "Emotional":
            emotional += 15

        if conflict == "Internal":
            character += 10

        if conflict == "Existential":
            originality += 10
            cinematic += 10

        if ending == "Twist Ending":
            originality += 5

        if ending == "Victory Climax":
            commercial += 10

        if ending == "Emotional Resolution":
            emotional += 5

        overall = round(
            (
                originality +
                emotional +
                character +
                commercial +
                cinematic
            ) / 5
        )

        return {
            "originality": originality,
            "emotional_impact": emotional,
            "character_depth": character,
            "commercial_appeal": commercial,
            "cinematic_potential": cinematic,
            "overall": overall
        }