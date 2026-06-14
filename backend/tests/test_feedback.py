from app.services.script_analysis_service import (
    ScriptAnalysisService
)

from app.services.feedback_service import (
    FeedbackService
)

analysis_service = (
    ScriptAnalysisService()
)

feedback_service = (
    FeedbackService()
)

script = """

A man suffering from memory loss
tries to uncover hidden truths
about a mysterious murder.

"""

analysis = (
    analysis_service.analyze_script(
        script
    )
)

feedback = (
    feedback_service.generate_feedback(
        analysis
    )
)

print(feedback)