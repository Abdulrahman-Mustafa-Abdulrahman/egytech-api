import pytest
from .models import ParticipantsQueryParams, StatsQueryParams


class TestParticipantsQueryParams:

    def test_model_creation_and_deserialization_empty(self):
        participants = ParticipantsQueryParams()
        assert participants.model_dump(mode="json", exclude_none=True) == {}

    def test_model_creation_and_deserialization_with_params(self):
        participants = ParticipantsQueryParams(
            title="data_engineer",
            level="senior",
            min_yoe=2,
            max_yoe=5
        )
        assert participants.model_dump(mode="json", exclude_none=True) == {
            "title": "data_engineer",
            "level": "senior",
            "min_yoe": 2,
            "max_yoe": 5
        }

    def test_model_creation_and_deserialization_with_wrong_enums(self):
        with pytest.raises(ValueError):
            ParticipantsQueryParams(
                title="wrong_data",
                level="senoir",
                min_yoe=27,
                max_yoe=27,
            )

    def test_model_creation_and_deserialization_with_wrong_types(self):
        with pytest.raises(ValueError):
            ParticipantsQueryParams(
                title=["data_engineer"],
                level="intern",
                min_yoe=2,
                max_yoe=5,
            )

    def test_model_creation_and_deserialization_with_wrong_fields(self):
        with pytest.raises(ValueError):
            ParticipantsQueryParams(
                programming_language="python"
            )


class TestStatsQueryParams:

    def test_model_creation_and_deserialization_empty(self):
        stats = StatsQueryParams()
        assert stats.model_dump(mode="json", exclude_none=True) == {}

    def test_model_creation_and_deserialization_with_params(self):
        stats = StatsQueryParams(
            title="data_engineer",
            level="senior",
            min_yoe=2,
            max_yoe=5
        )
        assert stats.model_dump(mode="json", exclude_none=True) == {
            "title": "data_engineer",
            "level": "senior",
            "min_yoe": 2,
            "max_yoe": 5
        }

    def test_model_creation_and_deserialization_with_wrong_enums(self):
        with pytest.raises(ValueError):
            StatsQueryParams(
                title="wrong_data",
                level="senoir",
                min_yoe=27,
                max_yoe=27,
            )

    def test_model_creation_and_deserialization_with_wrong_types(self):
        with pytest.raises(ValueError):
            StatsQueryParams(
                title=["data_engineer"],
                level="intern",
                min_yoe=2,
                max_yoe=5,
            )

    def test_model_creation_and_deserialization_with_wrong_fields(self):
        with pytest.raises(ValueError):
            StatsQueryParams(
                wrong_field="python"
            )
