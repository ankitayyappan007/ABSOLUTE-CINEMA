from app.services.pulsegraph_service import PulseGraphService


service = PulseGraphService()

pulse = service.get_pulsegraph("Memento")

print("\nMEMENTO PULSEGRAPH:\n")

print(pulse)