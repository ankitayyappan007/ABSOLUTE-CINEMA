from fastapi import APIRouter
from pydantic import BaseModel

from app.services.script_analysis_service import (
    ScriptAnalysisService
)

from app.services.consultation_report_service import (
    ConsultationReportService
)

router = APIRouter()

analysis_service = (
    ScriptAnalysisService()
)

consultation_service = (
    ConsultationReportService()
)


class ScriptRequest(BaseModel):

    script_text: str


@router.post("/analyze-script")
def analyze_script(
    request: ScriptRequest
):

    return (
        analysis_service.analyze_script(
            request.script_text
        )
    )


@router.post("/consultation-report")
def consultation_report(
    request: ScriptRequest
):

    report = (
        consultation_service.generate_report(
            request.script_text
        )
    )

    return {
        "report": report
    }