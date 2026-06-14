from app.services.pulsegraph_service import (
    PulseGraphService
)


class PulseGraphFusionService:

    def __init__(self):

        self.pulse_service = PulseGraphService()

    def fuse_pulsegraphs(self, movie_titles):

        pulsegraphs = []

        for title in movie_titles:

            graph = self.pulse_service.get_pulsegraph(
                title
            )

            if graph:

                pulsegraphs.append(graph)

        if not pulsegraphs:

            return None

        fused_graph = []

        graph_length = len(
            pulsegraphs[0]
        )

        for i in range(graph_length):

            total = 0

            for graph in pulsegraphs:

                total += graph[i]

            average = round(
                total / len(pulsegraphs)
            )

            fused_graph.append(average)

        return fused_graph