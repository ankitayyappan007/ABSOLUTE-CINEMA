from app.services.fusion_service import FusionService
from app.services.blueprint_service import BlueprintService
from app.services.cinematic_narrator import CinematicNarrator


fusion_service = FusionService()

blueprint_service = BlueprintService()

narrator = CinematicNarrator()

fused_dna = fusion_service.fuse_movies([
    "Memento",
    "Interstellar",
    "KGF"
])

blueprint = blueprint_service.generate_blueprint(
    fused_dna
)

narration = narrator.narrate(blueprint)

print("\nABSOLUTE CINEMA NARRATION:\n")

print(narration)