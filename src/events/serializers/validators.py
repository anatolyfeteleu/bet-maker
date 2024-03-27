from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

from src.events.enums import EventResultEnum


def check_available_event_result(val: str):
    assert val in (EventResultEnum.LOSE, EventResultEnum.WIN)
    return val


EventResult = Annotated[str, AfterValidator(check_available_event_result)]
