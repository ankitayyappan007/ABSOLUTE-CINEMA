from app.services.script_analysis_service import (
    ScriptAnalysisService
)

service = ScriptAnalysisService()

result = service.analyze_script(
    """
    A man suffering from memory loss
    tries to uncover hidden truths
    about a mysterious murder.
    """
)

print(result)