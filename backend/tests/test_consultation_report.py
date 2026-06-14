from app.services.consultation_report_service import (
    ConsultationReportService
)

service = (
    ConsultationReportService()
)

script = """

A man suffering from memory loss
tries to uncover hidden truths
about a mysterious murder.

"""

report = (
    service.generate_report(
        script
    )
)

print(report)