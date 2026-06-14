from app.services.trait_interpreter import TraitInterpreter


class BlueprintService:

    def __init__(self):

        self.interpreter = TraitInterpreter()

    def generate_blueprint(self, fused_dna):

        blueprint = {}

        blueprint["structure"] = (
            "The story combines "
            + ", ".join(fused_dna["structure"])
            + " storytelling structures."
        )

        interpreted_tones = (
            self.interpreter.interpret_tones(
                fused_dna["tone"]
            )
        )

        blueprint["tone"] = (
            "The narrative "
            + ", while also ".join(interpreted_tones)
            + "."
        )

        blueprint["pace"] = (
            "The pacing evolves through "
            + ", ".join(fused_dna["pace"])
            + " progression."
        )

        blueprint["conflict"] = (
            "The protagonist faces "
            + ", ".join(fused_dna["conflict"])
            + " forms of conflict."
        )

        blueprint["ending"] = (
            "The climax blends "
            + ", ".join(fused_dna["ending"])
            + " storytelling payoffs."
        )

        blueprint["protagonist_arc"] = (
            "The protagonist journey reflects "
            + ", ".join(fused_dna["protagonist_arc"])
            + "."
        )

        return blueprint