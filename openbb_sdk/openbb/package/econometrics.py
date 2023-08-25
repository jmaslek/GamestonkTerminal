### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import Union

import openbb_core.app.model.results.empty
import openbb_provider
import openbb_provider.abstract.data
import pandas
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_inputs
from pydantic import validate_arguments


class CLASS_econometrics(Container):
    """/econometrics
    show
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def show(
        self,
        data: Union[openbb_provider.abstract.data.Data, pandas.DataFrame],
        chart: bool = False,
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            data=data,
            chart=chart,
        )

        return self._command_runner.run(
            "/econometrics/show",
            **inputs,
        )
