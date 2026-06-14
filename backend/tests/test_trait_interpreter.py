from app.services.trait_interpreter import TraitInterpreter


interpreter = TraitInterpreter()

tones = [
    "Psychological",
    "Emotional",
    "Aggressive"
]

results = interpreter.interpret_tones(
    tones
)

print("\nINTERPRETED TONES:\n")

for item in results:

    print("-", item)