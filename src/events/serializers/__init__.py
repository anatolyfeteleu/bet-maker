from pydantic import BaseModel, ConfigDict

from src.events.enums import EventResultEnum
from src.events.serializers.validators import EventResult


class EventBaseSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class EventListSerializer(EventBaseSerializer):
    result: EventResultEnum


class EventDetailSerializer(EventBaseSerializer):
    result: EventResultEnum


class EventShortSerializer(EventBaseSerializer):
    result: EventResultEnum


class EventUpdateSerializer(BaseModel):
    result: EventResult
