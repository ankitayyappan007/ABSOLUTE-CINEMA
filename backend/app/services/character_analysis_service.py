class CharacterAnalysisService:

    def analyze_character(
        self,
        dna
    ):

        arc = dna[
            "protagonist_arc"
        ][0][0]

        if arc == "Mental Collapse":

            return {

                "archetype":
                    "Tragic Hero",

                "strengths": [

                    "Highly determined",

                    "Intelligent thinker"
                ],

                "weaknesses": [

                    "Obsessive behavior",

                    "Emotionally isolated"
                ],

                "arc":
                    "Mental Collapse"
            }

        if arc == "Self Sacrifice":

            return {

                "archetype":
                    "Selfless Hero",

                "strengths": [

                    "Compassionate",

                    "Courageous"
                ],

                "weaknesses": [

                    "Self-neglect",

                    "Emotional burden"
                ],

                "arc":
                    "Self Sacrifice"
            }

        if arc == "Power Ascension":

            return {

                "archetype":
                    "Conqueror",

                "strengths": [

                    "Ambitious",

                    "Resilient"
                ],

                "weaknesses": [

                    "Arrogance",

                    "Power obsession"
                ],

                "arc":
                    "Power Ascension"
            }

        return {

            "archetype":
                "Classic Protagonist",

            "strengths": [

                "Determined"
            ],

            "weaknesses": [

                "Flawed"
            ],

            "arc":
                arc
        }