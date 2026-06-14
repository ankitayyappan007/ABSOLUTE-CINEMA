from app.services.fusion_service import FusionService
from app.services.trait_interpreter import TraitInterpreter


fusion_service = FusionService()

interpreter = TraitInterpreter()

fused_dna = fusion_service.fuse_movies([
    "Memento",
    "Interstellar",
    "KGF"
])

tone_descriptions = interpreter.interpret_tones(
    fused_dna["tone"]
)

print("\nINTERPRETED FUSED TONES:\n")

for description in tone_descriptions:

    print("-", description)