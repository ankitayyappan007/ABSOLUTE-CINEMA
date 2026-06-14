from app.services.pulsegraph_service import (
    PulseGraphService
)


class PriorityPulseGraphFusionService:

    def __init__(self):

        self.pulse_service = PulseGraphService()

    def fuse_with_priority(
        self,
        movie_weights
    ):

        pulsegraphs = []

        weights = []

        for movie, weight in movie_weights.items():

            graph = (
                self.pulse_service
                .get_pulsegraph(movie)
            )

            if graph:

                pulsegraphs.append(graph)

                weights.append(
                    weight / 100
                )

        if not pulsegraphs:

            return None

        fused_graph = []

        graph_length = len(
            pulsegraphs[0]
        )

        for i in range(graph_length):

            weighted_sum = 0

            for graph, weight in zip(
                pulsegraphs,
                weights
            ):

                weighted_sum += (
                    graph[i] * weight
                )

            fused_graph.append(
                round(weighted_sum)
            )

        return fused_graph