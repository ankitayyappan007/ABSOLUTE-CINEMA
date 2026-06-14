from app.services.fusion_service import FusionService
from app.services.blueprint_service import BlueprintService


fusion_service = FusionService()

blueprint_service = BlueprintService()

fused_dna = fusion_service.fuse_movies([
    "Memento",
    "Interstellar",
    "KGF"
])

blueprint = blueprint_service.generate_blueprint(
    fused_dna
)

print("\nABSOLUTE CINEMA BLUEPRINT:\n")

for key, value in blueprint.items():

    print(f"{key.upper()}:\n{value}\n")