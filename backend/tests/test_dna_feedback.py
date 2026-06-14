from app.services.dna_feedback_service import (
    DNAFeedbackService
)

service = (
    DNAFeedbackService()
)

report = (
    service.generate_dna_feedback(
        "Memento"
    )
)

print(report)