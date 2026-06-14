class FeedbackService:

    def generate_feedback(
        self,
        analysis_result
    ):

        movie = (
            analysis_result[
                "most_similar_movie"
            ]
        )

        genre = (
            analysis_result[
                "genre"
            ]
        )

        score = (
            analysis_result[
                "similarity_score"
            ]
        )

        if score >= 0.60:

            assessment = (
                "Strong narrative alignment."
            )

        elif score >= 0.40:

            assessment = (
                "Moderate narrative alignment."
            )

        else:

            assessment = (
                "Unique narrative direction."
            )

        report = f"""

Story Analysis Report

Closest Match:
{movie}

Genre:
{genre}

Similarity Score:
{score}

Narrative Assessment:
{assessment}

Key Strength:
The concept presents a recognizable narrative foundation that audiences can immediately understand.

Audience Appeal:
Likely to attract viewers who enjoy {genre.lower()} stories.

"""

        return report