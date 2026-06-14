from app.services.priority_pulsegraph_fusion_service import (
    PriorityPulseGraphFusionService
)

service = (
    PriorityPulseGraphFusionService()
)

result = service.fuse_with_priority({

    "Memento": 80,

    "Interstellar": 15,

    "KGF": 5
})

print(
    "\nPRIORITY PULSEGRAPH:\n"
)

print(result)