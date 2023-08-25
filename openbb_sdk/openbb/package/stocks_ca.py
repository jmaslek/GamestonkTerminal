### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import List, Literal, Optional, Union

import openbb_core.app.model.command_context
import openbb_core.app.model.results.empty
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_inputs
from pydantic import BaseModel, validate_arguments
from typing_extensions import Annotated


class CLASS_stocks_ca(Container):
    """/stocks/ca
    balance
    cashflow
    hcorr
    hist
    income
    peers
    scorr
    screener
    sentiment
    similar
    volume
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate_arguments
    def balance(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company balance sheet."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/balance",
            **inputs,
        )

    @validate_arguments
    def cashflow(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company cashflow."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/cashflow",
            **inputs,
        )

    @validate_arguments
    def hcorr(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company historical correlation."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/hcorr",
            **inputs,
        )

    @validate_arguments
    def hist(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company historical prices."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/hist",
            **inputs,
        )

    @validate_arguments
    def income(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company income statement."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/income",
            **inputs,
        )

    @validate_arguments
    def peers(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[BaseModel]:
        """Company peers.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[StockPeers]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            metadata: Optional[Metadata]
                Metadata info about the command execution.

        StockPeers
        ----------
        symbol : Optional[str]
            Symbol representing the entity requested in the data.
        peers_list : Optional[List[str]]
            A list of stock peers based on sector, exchange and market cap."""  # noqa: E501

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
            },
            extra_params=kwargs,
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/peers",
            **inputs,
        )

    @validate_arguments
    def scorr(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company sector correlation."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/scorr",
            **inputs,
        )

    @validate_arguments
    def screener(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company screener."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/screener",
            **inputs,
        )

    @validate_arguments
    def sentiment(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company sentiment."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/sentiment",
            **inputs,
        )

    @validate_arguments
    def similar(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company similar."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/similar",
            **inputs,
        )

    @validate_arguments
    def volume(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Company volume."""  # noqa: E501

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/ca/volume",
            **inputs,
        )