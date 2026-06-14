from app.services.dna_service import DNAService


service = DNAService()

dna = service.get_movie_dna("Memento")

print("\nMEMENTO STORY DNA:\n")

for key, value in dna.items():

    print(f"{key}: {value}")