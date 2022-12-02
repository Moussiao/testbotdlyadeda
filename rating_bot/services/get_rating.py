from collections import Counter
from dataclasses import dataclass
from typing import Dict

User = str
Evaluation = int
Ratings = Dict[User, Evaluation]

MIN_EVALUATION = 1
MAX_EVALUATION = 10


@dataclass
class RatingResult:
    users_count: int = 0
    final_grade: float = 0.0
    most_evaluation: int = 0
    most_evaluation_count: int = 0


EMPTY_RATING_RESULT = RatingResult()


def get_rating_result(ratings: Ratings) -> RatingResult:
    valid_evaluations = tuple(
        x for x in ratings.values() if MIN_EVALUATION <= x <= MAX_EVALUATION
    )
    if not valid_evaluations:
        return EMPTY_RATING_RESULT

    users_count = len(valid_evaluations)
    sum_evaluations = sum(valid_evaluations)
    final_grade = sum_evaluations / users_count if users_count else 0

    evaluations_counter = Counter(valid_evaluations)
    most_evaluation, most_evaluation_count = evaluations_counter.most_common(1)[0]

    return RatingResult(
        users_count=users_count,
        final_grade=final_grade,
        most_evaluation=most_evaluation,
        most_evaluation_count=most_evaluation_count,
    )
