from app.services.priority_fusion_service import (
    PriorityFusionService
)

from app.services.priority_pulsegraph_fusion_service import (
    PriorityPulseGraphFusionService
)


class StoryProfileService:

    def __init__(self):

        self.priority_fusion = (
            PriorityFusionService()
        )

        self.priority_pulse = (
            PriorityPulseGraphFusionService()
        )

    def generate_profile(
        self,
        movie_weights
    ):

        dna = (
            self.priority_fusion
            .fuse_with_priority(
                movie_weights
            )
        )

        pulsegraph = (
            self.priority_pulse
            .fuse_with_priority(
                movie_weights
            )
        )

        profile = {

            "dna": dna,

            "pulsegraph": pulsegraph
        }

        return profile