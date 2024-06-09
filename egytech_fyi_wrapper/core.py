import tomli
from .models import *
from typing import Optional, Dict, Any, ClassVar, Union, Self
import httpx
import pandas as pd
from pydantic import BaseModel, Field, computed_field, ConfigDict, model_validator


class Participants(ParticipantsQueryParams):
    model_config = ConfigDict(arbitrary_types_allowed=True, use_enum_values=True)
    participants: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.execute_call()

    def execute_call(self):
        url = "https://api.egytech.fyi/participants"
        headers = {"accept": "application/json"}

        response = httpx.get(url,
                             headers=headers,
                             params=self.model_dump(mode="json", exclude_none=True)
                             )

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        participants_dict = response.json()["results"]

        self.participants = pd.DataFrame.from_records(participants_dict)

    def get_df(self):
        return self.participants

    def save_csv(self, filename: str):
        self.participants.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.participants.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class Stats(StatsQueryParams):
    model_config = ConfigDict(arbitrary_types_allowed=True, use_enum_values=True)
    stats: Optional[Dict[str, str]] = Field(default=None, exclude=True)
    buckets: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.execute_call()

    def execute_call(self):
        url = "https://api.egytech.fyi/stats"
        headers = {"accept": "application/json"}

        response = httpx.get(url, headers=headers, params=self.model_dump(mode="json", exclude_none=True))

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        deser_response = response.json()

        self.buckets = pd.DataFrame.from_records(deser_response["buckets"])
        self.stats = deser_response["stats"]

    def get_stats(self):
        return self.stats

    def get_df(self):
        return self.buckets

    def save_csv(self, filename: str):
        self.buckets.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.buckets.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class PoolingClient(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    queries: list[ParticipantsQueryParams] = Field(exclude=True)
    dataframe: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.make_calls()

    def make_calls(self):
        url = "https://api.egytech.fyi/"
        headers = {"accept": "application/json"}

        with httpx.Client(base_url=url) as client:
            responses = []
            for query in self.queries:
                response = client.get("participants",
                                      headers=headers,
                                      params=query.model_dump(mode="json", exclude_none=True)
                                      )

                if response.status_code != 200:
                    raise Exception("Unsuccessful API Call")

                deser_response = response.json()
                responses.extend(list(deser_response.values())[-1])

        self.dataframe = pd.DataFrame.from_records(responses)

    def get_df(self):
        return self.dataframe

    def save_csv(self, filename: str):
        self.dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.dataframe.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")
