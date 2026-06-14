from app.services.priority_fusion_service import PriorityFusionService


service = PriorityFusionService()

result = service.fuse_with_priority({

    "Memento": 80,
    "Interstellar": 15,
    "KGF": 5
})

print("\nPRIORITIZED STORY DNA:\n")

for key, values in result.items():

    print(f"{key.upper()}")

    for trait, weight in values:

        print(f"  {trait} -> {weight}%")

    print()