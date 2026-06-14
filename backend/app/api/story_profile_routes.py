from fastapi import APIRouter
from pydantic import BaseModel

from app.services.story_profile_service import (
    StoryProfileService
)

router = APIRouter()

profile_service = StoryProfileService()


class StoryRequest(BaseModel):

    movie_weights: dict


@router.post("/story-profile")
def story_profile(
    request: StoryRequest
):

    profile = (
        profile_service.generate_profile(
            request.movie_weights
        )
    )

    return profile