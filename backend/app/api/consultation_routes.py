from fastapi import APIRouter
from pydantic import BaseModel


from app.services.script_analysis_service import (
    ScriptAnalysisService
)

from app.services.dna_service import (
    DNAService
)

from app.services.story_profile_service import (
    StoryProfileService
)

from app.services.movie_weight_service import (
    MovieWeightService
)

from app.services.recommendation_service import (
    RecommendationService
)

from app.services.scorecard_service import (
    ScorecardService
)

from app.services.story_blueprint_service import (
    StoryBlueprintService
)

from app.services.character_analysis_service import (
    CharacterAnalysisService
)

from app.services.theme_analysis_service import (
    ThemeAnalysisService
)

from app.services.originality_report_service import (
    OriginalityReportService
)

router = APIRouter()

analysis_service = ScriptAnalysisService()
dna_service = DNAService()
profile_service = StoryProfileService()
weight_service = MovieWeightService()
recommendation_service = (
    RecommendationService()
)
scorecard_service = (
    ScorecardService()
)
blueprint_service = (
    StoryBlueprintService()
)

character_service = (
    CharacterAnalysisService()
)

theme_service = (
    ThemeAnalysisService()
)

originality_service = (
    OriginalityReportService()
)

class ScriptRequest(BaseModel):
    script_text: str


@router.post("/consultation-report-v2")
def consultation_report_v2(
    request: ScriptRequest
):

    analysis = (
        analysis_service.analyze_script(
            request.script_text
        )
    )

    movie_title = (
        analysis["most_similar_movie"]
    )

    dna = (
        dna_service.get_movie_dna(
            movie_title
        )
    )

    return {

        "closest_match":
            analysis[
                "most_similar_movie"
            ],

        "genre":
            analysis[
                "genre"
            ],

        "similarity_score":
            analysis[
                "similarity_score"
            ],

        "dna":
            dna
    }


@router.post("/consultation-report-v3")
def consultation_report_v3(
    request: ScriptRequest
):

    analysis = (
        analysis_service.analyze_script(
            request.script_text
        )
    )

    movie_title = (
        analysis["most_similar_movie"]
    )

    dna = (
        dna_service.get_movie_dna(
            movie_title
        )
    )

    profile = (
        profile_service.generate_profile(
            {
                movie_title: 100
            }
        )
    )

    return {

        "closest_match":
            movie_title,

        "genre":
            analysis["genre"],

        "similarity_score":
            analysis[
                "similarity_score"
            ],

        "dna":
            dna,

        "pulsegraph":
            profile["pulsegraph"]
    }
    
@router.post("/consultation-report-v4")
def consultation_report_v4(
    request: ScriptRequest
):

    analysis = (
        analysis_service.analyze_script(
            request.script_text
        )
    )

    top_matches = (
        analysis["top_matches"]
    )

    weights = (
        weight_service.generate_weights(
            top_matches
        )
    )

    profile = (
        profile_service.generate_profile(
            weights
        )
    )
    
    feedback = (
    recommendation_service
    .generate_feedback(
        profile["dna"]
    )
    )
    
    scorecard = (
    scorecard_service
    .generate_scorecard(
        profile["dna"]
    )
)
    blueprint = (
    blueprint_service
    .generate_blueprint(
        profile["dna"]
    )
)
    character_profile = (
    character_service
    .analyze_character(
        profile["dna"]
    )
)

    theme_analysis = (
    theme_service
    .analyze_themes(
        profile["dna"]
    )
)
    originality_report = (
    originality_service
    .generate_report(
        weights,
        profile["dna"],
        scorecard
    )
)

    return {

        "closest_match":
            analysis[
                "most_similar_movie"
            ],

        "genre":
            analysis[
                "genre"
            ],

        "similarity_score":
            analysis[
                "similarity_score"
            ],

        "top_matches":
            top_matches,

        "weights":
            weights,

        "dna":
            profile["dna"],

    "pulsegraph":
    profile["pulsegraph"],
    
"feedback":
    feedback,

"scorecard":
    scorecard,

"blueprint":
    blueprint,
    

"character_profile":
    character_profile,

"theme_analysis":
    theme_analysis,


"originality_report":
    originality_report
    }