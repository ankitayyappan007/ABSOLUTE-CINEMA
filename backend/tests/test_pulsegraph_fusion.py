from app.services.pulsegraph_fusion_service import (
    PulseGraphFusionService
)

service = PulseGraphFusionService()

result = service.fuse_pulsegraphs([

    "Memento",
    "Interstellar",
    "KGF"
])

print("\nFUSED PULSEGRAPH:\n")

print(result)