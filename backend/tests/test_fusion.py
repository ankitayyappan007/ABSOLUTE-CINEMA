from app.services.fusion_service import FusionService


service = FusionService()

fusion_result = service.fuse_movies([
    "Memento",
    "Interstellar",
    "KGF"
])

print("\nFUSED STORY DNA:\n")

for key, values in fusion_result.items():

    print(f"{key}: {values}")