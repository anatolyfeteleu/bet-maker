from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from src.events.serializers import EventDetailSerializer
from src.extensions.validators import PositiveDecimal
from src.predictions.enums import PredictionBetEnum, PredictionStatusEnum


class PredictionBaseSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created: datetime


class PredictionListSerializer(PredictionBaseSerializer):
    amount: float
    event_id: int
    status: str
    bet: PredictionBetEnum


class PredictionDetailSerializer(PredictionBaseSerializer):
    event: EventDetailSerializer
    amount: float
    status: PredictionStatusEnum
    bet: PredictionBetEnum


class PredictionCreateSerializer(BaseModel):
    amount: PositiveDecimal
    event_id: int
    bet: PredictionBetEnum
