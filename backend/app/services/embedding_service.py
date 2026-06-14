from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.data_loader import load_movies


class EmbeddingService:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embedding Model Loaded Successfully")

        self.movies = load_movies()

        self.movie_embeddings = self.generate_movie_embeddings()

    def generate_embedding(self, text):

        embedding = self.model.encode(text)

        return embedding

    def generate_movie_embeddings(self):

        summaries = []

        for movie in self.movies:

            summaries.append(movie["summary"])

        embeddings = self.model.encode(summaries)

        return embeddings

    def find_similar_movies(self, user_story):

        user_embedding = self.model.encode([user_story])

        similarity_scores = cosine_similarity(
            user_embedding,
            self.movie_embeddings
        )[0]

        results = []

        for index, score in enumerate(similarity_scores):

            results.append({
                "title": self.movies[index]["title"],
                "genre": self.movies[index]["genre"],
                "similarity": float(score)
            })

        results = sorted(
            results,
            key=lambda x: x["similarity"],
            reverse=True
        )

        return results