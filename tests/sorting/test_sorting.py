from src.sorting import sort_by
from tests.sorting.mocks_for_test_sorting import (
    JOBS,
    JOBS_DATE_POSTED,
    JOBS_MAX_SALARY,
    JOBS_MIN_SALARY,
)


def test_sort_by_criteria():
    sort_by(JOBS, "min_salary")
    assert JOBS == JOBS_MIN_SALARY

    sort_by(JOBS, "max_salary")
    assert JOBS == JOBS_MAX_SALARY

    sort_by(JOBS, "date_posted")
    assert JOBS == JOBS_DATE_POSTED
