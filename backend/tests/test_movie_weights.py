from app.services.movie_weight_service import (
    MovieWeightService
)

service = MovieWeightService()

top_matches = [

    {
        "title": "Memento",
        "similarity": 0.681
    },

    {
        "title": "KGF",
        "similarity": 0.2289
    },

    {
        "title": "Interstellar",
        "similarity": 0.1338
    }
]

weights = (
    service.generate_weights(
        top_matches
    )
)

print(
    "\nGENERATED WEIGHTS:\n"
)

print(weights)