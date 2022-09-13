import pytest
from src.brazilian_jobs import read_brazilian_file

BRAZILIAN_JOB = {
  "title": "Ux Designer",
  "salary": "3000",
  "type": " full time"
}


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    )
    for job in brazilian_jobs:
        assert job.keys() == BRAZILIAN_JOB.keys()
    with pytest.raises(
        FileNotFoundError,
        match="No such file or directory: 'tests/mocks/brazilians_jobs.cs'",
    ):
        read_brazilian_file("tests/mocks/brazilians_jobs.cs")
