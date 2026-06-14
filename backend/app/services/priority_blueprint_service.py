from app.services.trait_interpreter import TraitInterpreter


class PriorityBlueprintService:

    def __init__(self):

        self.interpreter = TraitInterpreter()

    def generate_priority_blueprint(self, prioritized_dna):

        tone_traits = prioritized_dna["tone"]

        sorted_traits = sorted(
            tone_traits,
            key=lambda x: x[1],
            reverse=True
        )

        primary_trait = sorted_traits[0][0]
        secondary_trait = sorted_traits[1][0]
        tertiary_trait = sorted_traits[2][0]

        descriptions = self.interpreter.interpret_tones([
            primary_trait,
            secondary_trait,
            tertiary_trait
        ])

        blueprint = f"""
The story is primarily a {primary_trait.lower()} narrative that {descriptions[0]}.

Supporting this foundation is a {secondary_trait.lower()} layer that {descriptions[1]}.

Subtle influences of {tertiary_trait.lower()} storytelling further {descriptions[2]}.
"""

        return blueprint