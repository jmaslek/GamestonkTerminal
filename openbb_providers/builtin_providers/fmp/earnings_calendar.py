"""FMP Earnings Calendar fetcher."""

# IMPORT STANDARD
from datetime import date as dateType
from typing import Dict, List, Optional

# IMPORT THIRD-PARTY
from builtin_providers.fmp.helpers import create_url, get_data_many
from openbb_provider.model.abstract.data import Data

# IMPORT INTERNAL
from openbb_provider.model.data.earnings_calendar import (
    EarningsCalendarData,
    EarningsCalendarQueryParams,
)
from openbb_provider.provider.abstract.fetcher import Fetcher
from openbb_provider.provider.provider_helpers import data_transformer


class FMPEarningsCalendarQueryParams(EarningsCalendarQueryParams):
    """FMP Earnings Calendar query.

    Source: https://site.financialmodelingprep.com/developer/docs/earnings-calendar-api/

    Parameter
    ---------
    symbol : str
        The symbol of the company.
    limit : int
    """

    __name__ = "FMPEarningsCalendarQueryParams"


class FMPEarningsCalendarData(Data):
    __name__ = "FMPEarningsCalendarData"

    date: dateType
    symbol: str
    eps: Optional[float]
    epsEstimated: Optional[float]
    time: str
    revenue: Optional[int]
    revenueEstimated: Optional[int]
    updatedFromDate: Optional[dateType]
    fiscalDateEnding: dateType


class FMPEarningsCalendarFetcher(
    Fetcher[
        EarningsCalendarQueryParams,
        EarningsCalendarData,
        FMPEarningsCalendarQueryParams,
        FMPEarningsCalendarData,
    ]
):
    @staticmethod
    def transform_query(
        query: EarningsCalendarQueryParams, extra_params: Optional[Dict] = None
    ) -> FMPEarningsCalendarQueryParams:
        return FMPEarningsCalendarQueryParams(symbol=query.symbol, limit=query.limit)

    @staticmethod
    def extract_data(
        query: FMPEarningsCalendarQueryParams, api_key: str
    ) -> List[FMPEarningsCalendarData]:
        url = create_url(
            3, f"historical/earning_calendar/{query.symbol}", api_key, query, ["symbol"]
        )
        return get_data_many(url, FMPEarningsCalendarData)

    @staticmethod
    def transform_data(
        data: List[FMPEarningsCalendarData],
    ) -> List[EarningsCalendarData]:
        return data_transformer(data, EarningsCalendarData)