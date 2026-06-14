class ThemeAnalysisService:

    def analyze_themes(
        self,
        dna
    ):

        tone = dna["tone"][0][0]

        conflict = dna["conflict"][0][0]

        if (
            tone == "Psychological"
            and conflict == "Internal"
        ):

            return {

                "themes": [

                    "Identity",

                    "Memory",

                    "Truth"
                ],

                "summary":

                    "The story explores identity and truth through a protagonist struggling with unreliable memories."
            }

        if (
            tone == "Emotional"
            and conflict == "Existential"
        ):

            return {

                "themes": [

                    "Sacrifice",

                    "Hope",

                    "Humanity"
                ],

                "summary":

                    "The story explores sacrifice and hope through characters willing to risk everything for humanity's future."
            }

        if (
            tone == "Aggressive"
            and conflict == "External"
        ):

            return {

                "themes": [

                    "Power",

                    "Ambition",

                    "Legacy"
                ],

                "summary":

                    "The story examines ambition and power as the protagonist fights to build a lasting legacy."
            }

        return {

            "themes": [

                "Growth",

                "Conflict",

                "Change"
            ],

            "summary":

                "The story follows a transformative journey driven by conflict and personal growth."
        }