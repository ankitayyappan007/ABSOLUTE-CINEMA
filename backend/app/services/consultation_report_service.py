from app.services.script_analysis_service import (
    ScriptAnalysisService
)

from app.services.feedback_service import (
    FeedbackService
)

from app.services.dna_feedback_service import (
    DNAFeedbackService
)


class ConsultationReportService:

    def __init__(self):

        self.analysis_service = (
            ScriptAnalysisService()
        )

        self.feedback_service = (
            FeedbackService()
        )

        self.dna_service = (
            DNAFeedbackService()
        )

    def generate_report(
        self,
        script_text
    ):

        analysis = (
            self.analysis_service
            .analyze_script(
                script_text
            )
        )

        feedback = (
            self.feedback_service
            .generate_feedback(
                analysis
            )
        )

        dna_feedback = (
            self.dna_service
            .generate_dna_feedback(
                analysis[
                    "most_similar_movie"
                ]
            )
        )

        report = f"""

ABSOLUTE CINEMA CONSULTATION REPORT

{feedback}

{dna_feedback}

"""

        return report