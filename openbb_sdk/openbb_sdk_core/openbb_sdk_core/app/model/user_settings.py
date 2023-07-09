from pydantic import Field

from openbb_sdk_core.app.model.abstract.tagged import Tagged
from openbb_sdk_core.app.model.credentials import Credentials
from openbb_sdk_core.app.model.defaults import Defaults
from openbb_sdk_core.app.model.preferences import Preferences
from openbb_sdk_core.app.model.profile import Profile


class UserSettings(Tagged):
    profile: Profile = Field(default_factory=Profile)
    credentials: Credentials = Field(default_factory=Credentials)
    preferences: Preferences = Field(default_factory=Preferences)
    defaults: Defaults = Field(default_factory=Defaults)

    def __repr__(self) -> str:
        return (
            self.__class__.__name__
            + "\n\n"
            + "\n".join([f"{k}: {v}" for k, v in self.dict().items()])
        )