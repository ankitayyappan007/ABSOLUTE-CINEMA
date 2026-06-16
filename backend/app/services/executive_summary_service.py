class ExecutiveSummaryService:

    def generate_summary(
        self,
        closest_match,
        scorecard,
        theme_analysis
    ):

        return (
            f"This story most closely resembles "
            f"{closest_match}. "
            f"It explores themes of "
            f"{', '.join(theme_analysis['themes'])}. "
            f"The project demonstrates strong originality "
            f"({scorecard['originality']}/100) and commercial appeal "
            f"({scorecard['commercial_appeal']}/100). "
            f"Further development should focus on emotional depth "
            f"and character complexity."
        )