from app.services.priority_fusion_service import (
    PriorityFusionService
)

from app.services.priority_blueprint_service import (
    PriorityBlueprintService
)


fusion = PriorityFusionService()

blueprint_service = PriorityBlueprintService()

prioritized_dna = fusion.fuse_with_priority({

    "Memento": 80,
    "Interstellar": 15,
    "KGF": 5
})

blueprint = (
    blueprint_service.generate_priority_blueprint(
        prioritized_dna
    )
)

print("\nPRIORITY BLUEPRINT:\n")

print(blueprint)