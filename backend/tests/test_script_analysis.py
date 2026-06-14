from app.services.script_analysis_service import (
    ScriptAnalysisService
)

service = (
    ScriptAnalysisService()
)

script = """

A man suffering from memory loss
tries to uncover hidden truths
about a mysterious murder.

"""

result = (
    service.analyze_script(
        script
    )
)

print(
    "\nSCRIPT ANALYSIS:\n"
)

print(result)