from typing import TYPE_CHECKING, List

from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.events.enums import EventResultEnum
from src.extensions.models import BaseModelMixin

if TYPE_CHECKING:
    from src.predictions.models import Prediction


class Event(BaseModelMixin, Base):
    __tablename__ = "events"

    result: Mapped[str] = mapped_column(
        VARCHAR(10),
        nullable=False,
        default=EventResultEnum.PENDING,
        server_default=EventResultEnum.PENDING,
        info={"verbose_name": "Result"},
    )

    predictions: Mapped[List["Prediction"]] = relationship(
        back_populates="event"
    )
