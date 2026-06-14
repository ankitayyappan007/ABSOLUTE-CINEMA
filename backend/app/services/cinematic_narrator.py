class CinematicNarrator:

    def narrate(self, blueprint):

        narration = []

        structure_text = (
            "The narrative unfolds through "
            + blueprint["structure"]
            .replace("The story combines ", "")
            .replace(" storytelling structures.", "")
            + ", creating an unpredictable cinematic flow."
        )

        tone_text = (
            "Emotionally, the film carries "
            + blueprint["tone"]
            .replace("The narrative carries a ", "")
            .replace(" tonal identity.", "")
            + " energy throughout the experience."
        )

        pace_text = (
            "The pacing shifts dynamically, moving through "
            + blueprint["pace"]
            .replace("The pacing evolves through ", "")
            .replace(" progression.", "")
            + " rhythms."
        )

        conflict_text = (
            "At its core, the protagonist struggles against "
            + blueprint["conflict"]
            .replace("The protagonist faces ", "")
            .replace(" forms of conflict.", "")
            + " forces."
        )

        ending_text = (
            "The climax merges "
            + blueprint["ending"]
            .replace("The climax blends ", "")
            .replace(" storytelling payoffs.", "")
            + " into a layered cinematic payoff."
        )

        arc_text = (
            "The protagonist transformation reflects "
            + blueprint["protagonist_arc"]
            .replace("The protagonist journey reflects ", "")
            .replace(".", "")
            + "."
        )

        narration.append(structure_text)
        narration.append(tone_text)
        narration.append(pace_text)
        narration.append(conflict_text)
        narration.append(ending_text)
        narration.append(arc_text)

        final_narration = "\n\n".join(narration)

        return final_narration