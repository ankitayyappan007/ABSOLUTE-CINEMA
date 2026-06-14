from app.services.story_profile_service import (
    StoryProfileService
)

service = StoryProfileService()

profile = service.generate_profile({

    "Memento": 80,

    "Interstellar": 15,

    "KGF": 5
})

print(
    "\nSTORY PROFILE:\n"
)

print(profile)