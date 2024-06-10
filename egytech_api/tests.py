import pytest
from .models import ParticipantsQueryParams, StatsQueryParams
from pydantic import ValidationError
from contextlib import nullcontext


@pytest.mark.parametrize("normal, expected",
                         [({"title": "backend", "min_yoe": 2, "business_line": "b2b"},
                           nullcontext(ParticipantsQueryParams(
                               title="backend",
                               min_yoe=2,
                               business_line="b2b"
                           ))),
                          ({"title": "frontend", "level": "intern", "max_yoe": 0}, pytest.raises(ValidationError)),
                          ({"programming_language": "python"}, pytest.raises(ValidationError)),
                          ({"title": ["backend"]}, pytest.raises(ValidationError)),
                          ({"wrong_field": "backend"}, pytest.raises(ValueError)),
                          ])
class TestParticipantsQueryParams:

    def test_model_creation(self, normal, expected):
        with expected as e:
            participants = ParticipantsQueryParams(**normal)
            assert participants == e


@pytest.mark.parametrize("normal, expected",
                         [({"title": "backend", "min_yoe": 2, "business_line": "b2b"},
                           nullcontext(StatsQueryParams(
                               title="backend",
                               min_yoe=2,
                               business_line="b2b"
                           ))),
                          ({"title": "frontend", "level": "intern", "max_yoe": 0}, pytest.raises(ValueError)),
                          ({"programming_language": "python"},
                           nullcontext(StatsQueryParams(programming_language="python"))),
                          ({"title": ["backend"]}, pytest.raises(ValidationError)),
                          ({"wrong_field": "backend"}, pytest.raises(ValueError)),
                          ])
class TestStatsQueryParams:

    def test_model_creation(self, normal, expected):
        with expected as e:
            stats = StatsQueryParams(**normal)
            assert stats == e
