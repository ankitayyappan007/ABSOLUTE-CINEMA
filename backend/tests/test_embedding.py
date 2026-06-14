from app.services.embedding_service import EmbeddingService


service = EmbeddingService()

story = """
A man trapped in fragmented memories
tries to uncover hidden truths
while reality slowly collapses around him.
"""

results = service.find_similar_movies(story)

print("\nMOST SIMILAR STORIES:\n")

for movie in results:

    print(
        f"{movie['title']} "
        f"({movie['genre']}) "
        f"- Similarity Score: {movie['similarity']:.4f}"
    )