from app.services.data_loader import load_movies


movies = load_movies()

print("\nMOVIE DATA:\n")

for movie in movies:

    print(movie)