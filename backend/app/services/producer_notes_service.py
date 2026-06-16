class ProducerNotesService:

    def generate_notes(
        self,
        genre,
        scorecard
    ):

        budget_range = "Medium"

        if "Sci-Fi" in genre:

            budget_range = "High"

        if "Drama" in genre:

            budget_range = "Low"

        streaming_potential = (
            "High"
            if scorecard["overall"] >= 75
            else "Medium"
        )

        theatrical_potential = (
            "High"
            if scorecard["commercial_appeal"] >= 85
            else "Medium"
        )

        franchise_potential = (
            "High"
            if scorecard["cinematic_potential"] >= 85
            else "Low"
        )

        return {

            "budget_range":
                budget_range,

            "target_audience":
                "18-35",

            "streaming_potential":
                streaming_potential,

            "theatrical_potential":
                theatrical_potential,

            "franchise_potential":
                franchise_potential
        }