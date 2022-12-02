from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rating_bot.services import RatingResult


def get_start_rating_msg() -> str:
    return "ГОЛОСОВАНИЕ НАЧАЛОСЬ - ПИШИ ОТ 1 ДО 10"


def get_rating_result_msg(result: "RatingResult") -> str:
    return (
        f"Голосование окончено! "
        f"Средняя оценка: {result.final_grade:.1f} Больше всего "
        f"оценили на {result.most_evaluation}({result.most_evaluation_count}) "
        f"Количество оценивших: {result.users_count}"
    )


def get_test_msg() -> str:
    return "Test message"
