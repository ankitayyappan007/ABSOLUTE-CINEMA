from app.services.pulsegraph_visualizer import (
    PulseGraphVisualizer
)

from app.services.pulsegraph_fusion_service import (
    PulseGraphFusionService
)

fusion = PulseGraphFusionService()

visualizer = PulseGraphVisualizer()

pulsegraph = fusion.fuse_pulsegraphs([

    "Memento",
    "Interstellar",
    "KGF"
])

visualizer.create_graph(
    pulsegraph
)