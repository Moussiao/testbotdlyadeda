from rating_bot.services import get_rating_result


def test_get_rating() -> None:
    ratings = dict(
        test1=1,
        test2=2,
        test3=2,
        test4=3,
        test5=4,
        test6=4,
        test7=4,
        test8=5,
        test9=5,
        test10=5,
        tset11=5,
        test12=6,
        test13=7,
        test14=8,
        test15=9,
        test16=10,
    )

    result = get_rating_result(ratings)

    assert result.users_count == len(ratings)
    assert result.final_grade == 5
    assert result.most_evaluation == 5
    assert result.most_evaluation_count == 4


def test_empty_get_rating() -> None:
    ratings = {}

    result = get_rating_result(ratings)

    assert result.users_count == 0
    assert result.final_grade == 0.0
    assert result.most_evaluation == 0
    assert result.most_evaluation_count == 0


def test_not_valid_get_rating() -> None:
    ratings = dict(test=-1, test2=0, test3=11, test4=100, test5=-100, test6=50)

    result = get_rating_result(ratings)

    assert result.users_count == 0
    assert result.final_grade == 0.0
    assert result.most_evaluation == 0
    assert result.most_evaluation_count == 0


def test_with_not_valid_get_rating() -> None:
    ratings = dict(test=-1, test2=0, test3=11, test4=3, test5=3, test6=4, test7=5)

    result = get_rating_result(ratings)

    assert result.users_count == 4
    assert result.final_grade == 3.75
    assert result.most_evaluation == 3
    assert result.most_evaluation_count == 2


def test_only_one_get_rating() -> None:
    value = 1
    ratings = dict(test=value, test2=value, test3=value)

    result = get_rating_result(ratings)

    assert result.users_count == len(ratings)
    assert result.final_grade == value
    assert result.most_evaluation == value
    assert result.most_evaluation_count == len(ratings)


def test_only_ten_get_rating() -> None:
    value = 10
    ratings = dict(test=value, test2=value, test3=value)

    result = get_rating_result(ratings)

    assert result.users_count == len(ratings)
    assert result.final_grade == value
    assert result.most_evaluation == value
    assert result.most_evaluation_count == len(ratings)
