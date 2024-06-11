import asyncio
import asyncio
import itertools
from typing import Dict, Any

import httpx
import pandas as pd

from models import *


class Participants(ParticipantsQueryParams):
    """Class for retrieval of participants from the API with the given query parameters.

    Attributes
    ----------
    title : TitleEnum
        The job title of the participants.
    level : LevelEnum
        The job level of the participants.
    min_yoe : int
        The minimum years of experience of the participants.
    max_yoe : int
        The maximum years of experience of the participants.
    gender : GenderEnum
        The gender of the participants.
    cs_degree : DegreeType
        Whether the participants have a computer science degree.
    business_market : BusinessMarketEnum
        The market scope of the business of the participants.
    business_size : BusinessSizeEnum
        The size of the business of the participants.
    business_focus : BusinessFocusEnum
        The focus of the business of the participants.
    business_line : BusinessLineEnum
        The line of business of the participants.
    include_relocated : IncludeType
        Whether to include participants who have relocated.
    include_remote_abroad : IncludeType
        Whether to include participants who are remote abroad.
    participants : pd.DataFrame
        This is where the pandas.DataFrame resulting from the API Call is stored.

    Methods
    -------
    model_post_init(__context: Any)
        Placeholder that calls execute_call() on self with given query parameters after initialization of the pydantic
        model for the available query parameters.
    execute_call()
        Executes the API call with the given query parameters.
    get_df()
        Returns the pandas.DataFrame of the participants.
    save_csv(filename: str)
        Saves the participants DataFrame to a CSV file.
    save_excel(filename: str)
        Saves the participants DataFrame to an Excel file.

    """
    model_config = ConfigDict(arbitrary_types_allowed=True, use_enum_values=True, extra="forbid")
    participants: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        """
        Placeholder that calls execute_call() on self with given query parameters after initialization of the pydantic
        model for the available query parameters with the correct specification.

        Parameters
        ----------
        __context : Any

        Returns
        -------
        None
        """
        self.execute_call()

    def execute_call(self):
        """Executes the API call with the given query parameters during model initialization.

        Returns
        -------
        None
        """
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
        """Returns the pandas.DataFrame of the participants.

        Returns
        -------
        pd.DataFrame
        """
        return self.participants

    def save_csv(self, filename: str):
        """Saves the participants DataFrame to a CSV file.

        Parameters
        ----------
        filename : str
            The filename to save the CSV file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.csv".

        Returns
        -------
        None
        """
        self.participants.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        """Saves the participants DataFrame to an Excel file.

        Parameters
        ----------
        filename : str
            The filename to save the Excel file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.xlsx".

        Returns
        -------
        None
        """
        self.participants.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class Stats(StatsQueryParams):
    """Class for retrieval of statistics from the API with the given query parameters.

    Attributes
    ----------
    title : TitleEnum
        The job title of the participants.
    level : LevelEnum
        The job level of the participants.
    min_yoe : int
        The minimum years of experience of the participants.
    max_yoe : int
        The maximum years of experience of the participants.
    gender : GenderEnum
        The gender of the participants.
    cs_degree : DegreeType
        Whether the participants have a computer science degree.
    business_market : BusinessMarketEnum
        The market scope of the business of the participants.
    business_size : BusinessSizeEnum
        The size of the business of the participants.
    business_focus : BusinessFocusEnum
        The focus of the business of the participants.
    business_line : BusinessLineEnum
        The line of business of the participants.
    include_relocated : IncludeType
        Whether to include participants who have relocated.
    include_remote_abroad : IncludeType
        Whether to include participants who are remote abroad.
    programming_language : ProgrammingLanguageEnum
        The programming language of the participants.
    stats : Dict[str, str]
        The statistics from the API Call, including:
        - totalCount : str
            The total count of retrieved participants.
        - median : str
            The median compensation of retrieved participants.
        - p20Compensation : str
            The 20th percentile compensation of retrieved participants.
        - p75Compensation : str
            The 75th percentile compensation of retrieved participants.
        - p90Compensation : str
            The 90th percentile compensation of retrieved participants.
    buckets : pd.DataFrame
        The buckets of compensation of retrieved participants.

    Methods
    -------
    model_post_init(__context: Any)
        Placeholder that calls execute_call() on self with given query parameters after initialization of the pydantic
        model for the available query parameters.
    execute_call()
        Executes the API call with the given query parameters.
    get_stats()
        Returns the statistics from the API Call.
    get_df()
        Returns the pandas.DataFrame of the buckets.
    save_csv(filename: str)
        Saves the buckets DataFrame to a CSV file.
    save_excel(filename: str)
        Saves the buckets DataFrame to an Excel file.

    """
    model_config = ConfigDict(arbitrary_types_allowed=True, use_enum_values=True, extra="forbid")
    stats: Optional[Dict[str, str]] = Field(default=None, exclude=True)
    buckets: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        """Placeholder that calls execute_call() on self with given query parameters after initialization of the
        pydantic model for the available query parameters with the correct specification.

        Parameters
        ----------
        __context : Any

        Returns
        -------
        None

        """
        self.execute_call()

    def execute_call(self):
        """Executes the API call with the given query parameters during model initialization.

        Returns
        -------
        None

        """
        url = "https://api.egytech.fyi/stats"
        headers = {"accept": "application/json"}

        response = httpx.get(url, headers=headers, params=self.model_dump(mode="json", exclude_none=True))

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        deser_response = response.json()

        self.buckets = pd.DataFrame.from_records(deser_response["buckets"])
        self.stats = deser_response["stats"]

    def get_stats(self):
        """Returns the statistics from the API Call.

        Returns
        -------
        Dict[str, str]

        """
        return self.stats

    def get_df(self):
        """Returns the pandas.DataFrame of the buckets.

        Returns
        -------
        pd.DataFrame

        """
        return self.buckets

    def save_csv(self, filename: str):
        """Saves the buckets DataFrame to a CSV file.

        Parameters
        ----------
        filename : str
            The filename to save the CSV file to. This should not include the file extension.
            Example: "buckets" would lead to a file named "buckets.csv".

        Returns
        -------
        None

        """
        self.buckets.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        """Saves the buckets DataFrame to an Excel file.

        Parameters
        ----------
        filename : str
            The filename to save the Excel file to. This should not include the file extension.
            Example: "buckets" would lead to a file named "buckets.xlsx".

        Returns
        -------
        None

        """
        self.buckets.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class PoolingClient(BaseModel):
    """Class for pooling multiple API calls with different query parameters into one object.

    Attributes
    ----------
    queries : list[ParticipantsQueryParams]
        The list of query parameters for the participants endpoint.
    dataframe : pd.DataFrame
        The resulting pandas.DataFrame of the participants from the API Call.

    Methods
    -------
    model_post_init(__context: Any)
        Placeholder that calls make_calls() after initialization of the proper
        pydantic model for the available query parameters correctly.
    make_calls()
        Executes the API calls with the given query parameters.
    get_df()
        Returns the pandas.DataFrame of the aggregated participants from all the given queries.
    save_csv(filename: str)
        Saves the aggregated participants DataFrame to a CSV file.
    save_excel(filename: str)
        Saves the aggregated participants DataFrame to an Excel file.

    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    queries: list[ParticipantsQueryParams] = Field(exclude=True)
    dataframe: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        """Placeholder that calls make_calls() after initialization of the proper pydantic model for the
        available query parameters correctly.

        Parameters
        ----------
        __context : Any

        Returns
        -------
        None

        """
        self.make_calls()

    def make_calls(self):
        """Executes the API calls with the given query parameters.

        Returns
        -------
        None

        """
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
        """Returns the pandas.DataFrame of the aggregated participants from all the given queries.

        Returns
        -------
        pd.DataFrame

        """
        return self.dataframe

    def save_csv(self, filename: str):
        """Saves the aggregated participants DataFrame to a CSV file.

        Parameters
        ----------
        filename : str
            The filename to save the CSV file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.csv".

        Returns
        -------
        None

        """
        self.dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        """Saves the aggregated participants DataFrame to an Excel file.

        Parameters
        ----------
        filename : str
            The filename to save the Excel file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.xlsx".

        Returns
        -------
        None

        """
        self.dataframe.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")


class AsyncPoolingClient(BaseModel):
    """Class for asynchronously pooling multiple API calls with different query parameters into one object.

    Attributes
    ----------
    queries : list[ParticipantsQueryParams]
        The list of query parameters for the participants endpoint.
    dataframe : pd.DataFrame
        The resulting pandas.DataFrame of the participants from the API Call.

    Methods
    -------
    model_post_init(__context: Any)
        Placeholder that calls make_calls() after initialization of the proper
        pydantic model for the available query parameters correctly.
    make_calls()
        Asynchronously executes the API calls with the given query parameters while using connection pooling.
    get_df()
        Returns the pandas.DataFrame of the aggregated participants from all the given queries.
    save_csv(filename: str)
        Saves the aggregated participants DataFrame to a CSV file.
    save_excel(filename: str)
        Saves the aggregated participants DataFrame to an Excel file.

    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    queries: list[ParticipantsQueryParams] = Field(exclude=True)
    dataframe: Optional[pd.DataFrame] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        """Placeholder that calls make_calls() after initialization of the proper pydantic model for the
        available query parameters correctly.

        Parameters
        ----------
        __context : Any

        Returns
        -------
        None

        """
        asyncio.run(self.make_calls())

    async def make_calls(self):
        """Asynchronously Executes the API calls with the given query parameters.

                Returns
                -------
                None

                """

        async def make_single_call(query: ParticipantsQueryParams, c: httpx.AsyncClient):
            response = await c.get("participants",
                                   params=query.model_dump(mode="json", exclude_none=True)
                                   )
            if response.status_code != 200:
                raise Exception("Unsuccessful API Call")
            return response.json()["results"]

        headers = {"accept": "application/json"}
        client = httpx.AsyncClient(base_url="https://api.egytech.fyi/", headers=headers)
        responses = await asyncio.gather(*map(make_single_call, self.queries, itertools.repeat(client)))
        results = itertools.chain(*responses)
        await client.aclose()

        self.dataframe = pd.DataFrame.from_records(results)

    def get_df(self):
        """Returns the pandas.DataFrame of the aggregated participants from all the given queries.

        Returns
        -------
        pd.DataFrame

        """
        return self.dataframe

    def save_csv(self, filename: str):
        """Saves the aggregated participants DataFrame to a CSV file.

        Parameters
        ----------
        filename : str
            The filename to save the CSV file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.csv".

        Returns
        -------
        None

        """
        self.dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str):
        """Saves the aggregated participants DataFrame to an Excel file.

        Parameters
        ----------
        filename : str
            The filename to save the Excel file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.xlsx".

        Returns
        -------
        None

        """
        self.dataframe.to_excel(filename + ".xlsx", index=False, engine="xlsxwriter")
