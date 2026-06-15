from sentence_transformers import SentenceTransformer
from app.services.data_loader import load_movies
import pickle

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

movies = load_movies()

summaries = [
    movie["summary"]
    for movie in movies
]

embeddings = model.encode(summaries)

with open(
    "movie_embeddings.pkl",
    "wb"
) as f:
    pickle.dump(
        embeddings,
        f
    )

print("Embeddings saved.")