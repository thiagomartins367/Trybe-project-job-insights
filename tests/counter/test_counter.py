import pytest
from src.counter import count_ocurrences

PYTHON = "Python"
JAVASCRIPT = "JaVaScRiPt"
FILE_PATH = "src/jobs.csv"


def test_counter():
    assert count_ocurrences(FILE_PATH, PYTHON) == 1639
    assert count_ocurrences(FILE_PATH, JAVASCRIPT) == 122
    with pytest.raises(
        AttributeError, match="'bool' object has no attribute 'lower'"
    ):
        count_ocurrences(FILE_PATH, True)
    with pytest.raises(
        FileNotFoundError,
        match="No such file or directory: 'src/jobs.cs'",
    ):
        count_ocurrences("src/jobs.cs", PYTHON)
