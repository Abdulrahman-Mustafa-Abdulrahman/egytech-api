import tomli
from models import ParticipantsQueryParams, StatsQueryParams, EndpointEnum
from typing import Optional, Dict, Any, ClassVar
import httpx
import pandas as pd
from pydantic import BaseModel, Field

with open("config.toml", mode="rb") as f:
    config = tomli.load(f)


class Participants(ParticipantsQueryParams):

    @computed_field
    def participants(self) -> pd.DataFrame:
        url = config["URL"]["participants"]
        headers = {"accept": "application/json"}

        response = httpx.get(url,
                             headers=headers,
                             params=self.model_dump(mode="json", exclude_none=True)
                             ).json()["results"]

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        return pd.DataFrame.from_records(response)

    def get_df(self):
        return self.participants

    def save_csv(self, filename: str):
        self.participants.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.participants.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class Stats(StatsQueryParams):
    stats: Optional[Dict[str, int]] = Field(default=None, exclude=True)
    buckets: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        url = config["URL"]["stats"]
        headers = {"accept": "application/json"}

        response = httpx.get(url, headers=headers, params=self.model_dump(mode="json", exclude_none=True)).json()

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        self.buckets = pd.DataFrame.from_records(response["buckets"])
        self.stats = response["stats"]

    def get_stats(self):
        return self.stats

    def get_df(self):
        return self.buckets

    def save_csv(self, filename: str):
        self.buckets.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.buckets.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class PoolingClient(BaseModel):
    endpoint: EndpointEnum = Field(exclude=True)
    queries: Union[list[StatsQueryParams], list[ParticipantsQueryParams]] = Field(exclude=True)
    dataframe: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        url = config["URL"]["base"]
        headers = {"accept": "application/json"}

        with httpx.Client(base_url=url) as client:
            responses = []
            for query in self.queries:
                response = client.get(self.endpoint,
                                      headers=headers,
                                      params=query.model_dump(mode="json", exclude_none=True)
                                      ).json()

                if response.status_code != 200:
                    raise Exception("Unsuccessful API Call")

                responses.append(list(response.values())[-1])

        self.dataframe = pd.DataFrame.from_records(responses)

    @model_validator(mode="after")
    def validate_queries(self) -> PoolingClient:
        if self.endpoint == "participants":
            for query in self.queries:
                if not isinstance(query, ParticipantsQueryParams):
                    raise ValueError("""If you use Endpoint 'participants',
                     queries must be a list of ParticipantsQueryParams""")
        elif self.endpoint == "stats":
            for query in self.queries:
                if not isinstance(query, StatsQueryParams):
                    raise ValueError("""If you use Endpoint 'stats',
                     queries must be a list of StatsQueryParams""")
        return self

    def get_df(self):
        return self.dataframe

    def save_csv(self, filename: str):
        self.dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        self.dataframe.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")
