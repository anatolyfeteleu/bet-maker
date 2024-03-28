from collections import defaultdict
from enum import StrEnum

from src.events.models import EventResultEnum


class PredictionStatusEnum(StrEnum):
    PENDING: str = "pending"
    WIN: str = "win"
    LOSE: str = "lose"


class PredictionBetEnum(StrEnum):
    WIN: str = "win"
    LOSE: str = "lose"


EventPredictionBetResultMapper = defaultdict(
    lambda: None,
    **{
        EventResultEnum.WIN: PredictionBetEnum.WIN,
        EventResultEnum.LOSE: PredictionBetEnum.LOSE,
    }
)
