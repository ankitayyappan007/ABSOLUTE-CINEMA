class TraitInterpreter:

    def __init__(self):

        self.tone_map = {

            "Psychological":
            "explores fractured perception, memory, and mental instability",

            "Emotional":
            "focuses on sacrifice, relationships, and emotional resonance",

            "Aggressive":
            "drives the story through ambition, confrontation, and power struggles"
        }

    def interpret_tones(self, tones):

        descriptions = []

        for tone in tones:

            if tone in self.tone_map:

                descriptions.append(
                    self.tone_map[tone]
                )

        return descriptions