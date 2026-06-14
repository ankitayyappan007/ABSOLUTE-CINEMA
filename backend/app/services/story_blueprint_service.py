class StoryBlueprintService:

    def generate_blueprint(
        self,
        dna
    ):

        tone = dna["tone"][0][0]

        conflict = dna["conflict"][0][0]

        # Psychological Story

        if (
            tone == "Psychological"
            and conflict == "Internal"
        ):

            return {

                "act1": [

                    "Introduce flawed protagonist",

                    "Reveal psychological instability",

                    "Present mystery"
                ],

                "act2": [

                    "Uncover hidden truths",

                    "Blur reality and perception",

                    "Escalate mental conflict"
                ],

                "act3": [

                    "Major revelation",

                    "Psychological collapse",

                    "Twist ending"
                ]
            }

        # Emotional Story

        if (
            tone == "Emotional"
            and conflict == "Existential"
        ):

            return {

                "act1": [

                    "Establish emotional relationships",

                    "Introduce impossible challenge",

                    "Create personal stakes"
                ],

                "act2": [

                    "Explore sacrifice",

                    "Increase emotional distance",

                    "Raise existential questions"
                ],

                "act3": [

                    "Final sacrifice",

                    "Emotional reunion",

                    "Hopeful resolution"
                ]
            }

        # Action Story

        if (
            tone == "Aggressive"
            and conflict == "External"
        ):

            return {

                "act1": [

                    "Introduce underdog hero",

                    "Present powerful antagonist",

                    "Trigger revenge motivation"
                ],

                "act2": [

                    "Rise in power",

                    "Conquer obstacles",

                    "Build reputation"
                ],

                "act3": [

                    "Final showdown",

                    "Victory climax",

                    "Legacy established"
                ]
            }

        return {

            "act1": [
                "Introduce protagonist",
                "Establish conflict"
            ],

            "act2": [
                "Escalate stakes",
                "Develop character arc"
            ],

            "act3": [
                "Resolve conflict",
                "Deliver ending"
            ]
        }