import asyncio
import itertools
from typing import Any, Dict, Optional

import httpx
import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from models import ParticipantsQueryParams, StatsQueryParams


class Participants(ParticipantsQueryParams):
    """Class that acts as a client for retrieval of participants from the API with the given query parameters.

    Attributes
    ----------
    title : {None, 'ai_automation', 'backend', 'crm', 'data_analytics', 'data_engineer', 'data_scientist',\
    'devops_sre_platform', 'embedded', 'engineering_manager', 'executive', 'frontend', 'fullstack', 'hardware',\
    'mobile', 'product_manager', 'product_owner', 'research', 'scrum', 'security', 'system_arch', 'technical_support',\
    'testing', 'ui_ux'}
        The job title of the participants.
    level : {None, 'c_level', 'director', 'group_product_manager', 'intern', 'junior', 'manager', 'mid_level',\
    'principal', 'senior', 'senior_manager', 'senior_principal', 'senior_staff', 'staff', 'team_lead', 'vp'}
        The job level of the participants.
    min_yoe : int, optional
        The minimum years of experience of the participants, must be greater than 0 and lower than 20.
    max_yoe : int, optional
        The maximum years of experience of the participants, must be greater than 1 and lower than 26.
    gender : {None, 'male', 'female'}
        The gender of the participants.
    cs_degree : bool, optional
        Whether the participants have a computer science degree.
    business_market : {None, 'global', 'regional', 'local'}
        The market scope of the business of the participants.
    business_size : {None, 'small', 'medium', 'large'}
        The size of the business of the participants.
    business_focus : {None, 'product', 'software_house'}
        The focus of the business of the participants.
    business_line : {None, 'b2b', 'b2c', 'both'}
        The line of business of the participants.
    include_relocated : bool, optional
        Whether to include participants who have relocated.
    include_remote_abroad : bool, optional
        Whether to include participants who are work remotely for companies abroad.
    _participants : pd.DataFrame
        This is where the pandas.DataFrame resulting from the API Call is stored. It can be accessed using by calling
        the get_df() method on your instance of the class.

    Methods
    -------
    get_df()
        Returns the pandas.DataFrame of the retrieved participants.
    save_csv(filename: str="participants")
        Saves the participants DataFrame to a CSV file.
    save_excel(filename: str="participants")
        Saves the participants DataFrame to an Excel file.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True, use_enum_values=True, extra="forbid"
    )
    _participants: Optional[pd.DataFrame] = None

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

        response = httpx.get(
            url,
            headers=headers,
            params=self.model_dump(mode="json", exclude_none=True),
        )

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        participants_dict = response.json()["results"]

        self._participants = pd.DataFrame.from_records(participants_dict)

    def get_df(self):
        """Returns the pandas.DataFrame of the participants.

        Returns
        -------
        pd.DataFrame
        """
        return self._participants

    def save_csv(self, filename: str = "participants") -> None:
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
        self._participants.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str = "participants") -> None:
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
        self._participants.to_excel(
            filename + ".xlsx", index=False, engine="xlsxwriter"
        )


class Stats(StatsQueryParams):
    """Class for retrieval of statistics from the API with the given query parameters.

    Attributes
    ----------
    title : {None, 'ai_automation', 'backend', 'crm', 'data_analytics', 'data_engineer', 'data_scientist',\
    'devops_sre_platform', 'embedded', 'engineering_manager', 'executive', 'frontend', 'fullstack', 'hardware',\
    'mobile', 'product_manager', 'product_owner', 'research', 'scrum', 'security', 'system_arch', 'technical_support',\
    'testing', 'ui_ux'}
        The job title of the participants.
    level : {None, 'c_level', 'director', 'group_product_manager', 'intern', 'junior', 'manager', 'mid_level',\
    'principal', 'senior', 'senior_manager', 'senior_principal', 'senior_staff', 'staff', 'team_lead', 'vp'}
        The job level of the participants.
    min_yoe : int, optional
        The minimum years of experience of the participants, must be greater than 0 and lower than 20.
    max_yoe : int, optional
        The maximum years of experience of the participants, must be greater than 1 and lower than 26.
    gender : {None, 'male', 'female'}
        The gender of the participants.
    cs_degree : bool, optional
        Whether the participants have a computer science degree.
    business_market : {None, 'global', 'regional', 'local'}
        The market scope of the business of the participants.
    business_size : {None, 'small', 'medium', 'large'}
        The size of the business of the participants.
    business_focus : {None, 'product', 'software_house'}
        The focus of the business of the participants.
    business_line : {None, 'b2b', 'b2c', 'both'}
        The line of business of the participants.
    include_relocated : bool, optional
        Whether to include participants who have relocated.
    include_remote_abroad : bool, optional
        Whether to include participants who are work remotely for companies abroad.
    programming_language : {None, 'java_script', 'type_script', 'python', 'c_sharp', 'java', 'php', 'c_cplusplus',\
    'kotlin', 'swift', 'dart', 'go', 'r', 'scala', 'rust'}
        The programming language of the participants.
    _stats : Dict[str, str]
        The dictionary of statistics retrieved from the API Call. This can be accessed by calling the get_stats() method
        on your instance of the class.
    _buckets : pd.DataFrame
        The buckets of compensation of retrieved participants. This can be accessed by calling the get_df() method on
        your instance of the class.

    Methods
    -------
    get_stats()
        Returns the statistics from the API Call.
    get_df()
        Returns the pandas.DataFrame of the buckets.
    save_csv(filename: str="buckets")
        Saves the buckets DataFrame to a CSV file.
    save_excel(filename: str="buckets")
        Saves the buckets DataFrame to an Excel file.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True, use_enum_values=True, extra="forbid"
    )
    _stats: Optional[Dict[str, str]] = None
    _buckets: Optional[pd.DataFrame] = None

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

    def execute_call(self) -> None:
        """Executes the API call with the given query parameters during model initialization.

        Returns
        -------
        None

        """
        url = "https://api.egytech.fyi/stats"
        headers = {"accept": "application/json"}

        response = httpx.get(
            url,
            headers=headers,
            params=self.model_dump(mode="json", exclude_none=True),
        )

        if response.status_code != 200:
            raise Exception("Unsuccessful API Call")

        deser_response = response.json()

        self._buckets = pd.DataFrame.from_records(
            deser_response["buckets"]
        )
        self._stats = deser_response["stats"]

    def get_stats(self) -> Dict[str, str]:
        """Returns the statistics from the API Call.

        Returns
        -------
        Dict[str, str]

        """
        return self._stats

    def get_df(self) -> pd.DataFrame:
        """Returns the pandas.DataFrame of the buckets.

        Returns
        -------
        pd.DataFrame

        """
        return self._buckets

    def save_csv(self, filename: str) -> None:
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
        self._buckets.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str) -> None:
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
        self._buckets.to_excel(
            filename + ".xlsx", index=False, engine="xlsxwriter"
        )


class PoolingClient(BaseModel):
    """Class for pooling multiple API calls with different query parameters into one object.

    Attributes
    ----------
    queries : list of `ParticipantsQueryParams`
        The list of query parameters for the participants endpoint.
    _dataframe : pd.DataFrame
        The resulting pandas.DataFrame of the participants from the API Call. This can be accessed by calling the
        get_df() method on your instance of the class.

    Methods
    -------
    get_df()
        Returns the pandas.DataFrame of the aggregated participants from all the given queries.
    save_csv(filename: str="pooled_participants_results")
        Saves the aggregated participants DataFrame to a CSV file.
    save_excel(filename: str="pooled_participants_results")
        Saves the aggregated participants DataFrame to an Excel file.

    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    queries: list[ParticipantsQueryParams] = Field(exclude=True)
    _dataframe: Optional[pd.DataFrame] = None

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

    def make_calls(self) -> None:
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
                response = client.get(
                    "participants",
                    headers=headers,
                    params=query.model_dump(
                        mode="json", exclude_none=True
                    ),
                )

                if response.status_code != 200:
                    raise Exception("Unsuccessful API Call")

                deser_response = response.json()
                responses.extend(list(deser_response.values())[-1])

        self._dataframe = pd.DataFrame.from_records(responses)

    def get_df(self) -> pd.DataFrame:
        """Returns the pandas.DataFrame of the aggregated participants from all the given queries.

        Returns
        -------
        pd.DataFrame

        """
        return self._dataframe

    def save_csv(
            self, filename: str = "pooled_participants_results"
    ) -> None:
        """Saves the aggregated participants DataFrame to a CSV file.

        Parameters
        ----------
        filename : str = "pooled_participants_results"
            The filename to save the CSV file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.csv".

        Returns
        -------
        None

        """
        self._dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(
            self, filename: str = "pooled_participants_results"
    ) -> None:
        """Saves the aggregated participants DataFrame to an Excel file.

        Parameters
        ----------
        filename : str = "pooled_participants_results"
            The filename to save the Excel file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.xlsx".

        Returns
        -------
        None

        """
        self._dataframe.to_excel(
            filename + ".xlsx", index=False, engine="xlsxwriter"
        )


class AsyncPoolingClient(BaseModel):
    """Class for asynchronously pooling multiple API calls with different query parameters into one object.

    Attributes
    ----------
    queries : list of `ParticipantsQueryParams`
        The list of query parameters for the participants endpoint.
    _dataframe : pd.DataFrame
        The resulting pandas.DataFrame of the participants from the API Call.

    Methods
    -------
    get_df()
        Returns the `pandas.DataFrame` of the aggregated participants from all the given queries.
    save_csv(filename: str = "pooled_async_participants_results")
        Saves the aggregated participants DataFrame to a CSV file.
    save_excel(filename: str = "pooled_async_participants_results")
        Saves the aggregated participants DataFrame to an Excel file.

    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    queries: list[ParticipantsQueryParams] = Field(exclude=True)
    _dataframe: Optional[pd.DataFrame] = None

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

    async def make_calls(self) -> None:
        """Asynchronously Executes the API calls with the given query parameters.

        Returns
        -------
        None

        """

        async def make_single_call(
                query: ParticipantsQueryParams, c: httpx.AsyncClient
        ) -> list[Dict[str, Any]]:
            response = await c.get(
                "participants",
                params=query.model_dump(mode="json", exclude_none=True),
            )
            if response.status_code != 200:
                raise Exception("Unsuccessful API Call")
            return response.json()["results"]

        headers = {"accept": "application/json"}
        client = httpx.AsyncClient(
            base_url="https://api.egytech.fyi/", headers=headers
        )
        responses = await asyncio.gather(
            *map(make_single_call, self.queries, itertools.repeat(client))
        )
        results = itertools.chain(*responses)
        await client.aclose()

        self._dataframe = pd.DataFrame.from_records(results)

    def get_df(self) -> pd.DataFrame:
        """Returns the pandas.DataFrame of the aggregated participants from all the given queries.

        Returns
        -------
        pd.DataFrame

        """
        return self._dataframe

    def save_csv(self, filename: str) -> None:
        """Saves the aggregated participants DataFrame to a CSV file.

        Parameters
        ----------
        filename : str = "pooled_async_participants_results"
            The filename to save the CSV file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.csv".

        Returns
        -------
        None

        """
        self._dataframe.to_csv(filename + ".csv", index=False)

    def save_excel(self, filename: str) -> None:
        """Saves the aggregated participants DataFrame to an Excel file.

        Parameters
        ----------
        filename : str = "pooled_async_participants_results"
            The filename to save the Excel file to. This should not include the file extension.
            Example: "participants" would lead to a file named "participants.xlsx".

        Returns
        -------
        None

        """
        self._dataframe.to_excel(
            filename + ".xlsx", index=False, engine="xlsxwriter"
        )
