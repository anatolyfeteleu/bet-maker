import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import FLOAT, UUID, VARCHAR, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.extensions.models import BaseModelMixin
from src.predictions.enums import PredictionStatusEnum

if TYPE_CHECKING:
    from src.events.models import Event


class Prediction(BaseModelMixin, Base):
    __tablename__ = "predictions"

    uuid: Mapped[str] = mapped_column(
        UUID,
        nullable=False,
        default=uuid.uuid4,
        info={"verbose_name": "Unique identifier"},
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
        nullable=False,
        info={"verbose_name": "Event id"},
    )
    bet: Mapped[str] = mapped_column(
        VARCHAR(10),
        nullable=True,
        info={"verbose_name": "Bet"},
    )
    status: Mapped[str] = mapped_column(
        VARCHAR(10),
        nullable=False,
        default=PredictionStatusEnum.PENDING,
        info={"verbose_name": "Status"},
    )
    amount: Mapped[Decimal] = mapped_column(
        DECIMAL(8, 2),
        nullable=False,
        info={"verbose_name": "Bet amount"},
    )

    event: Mapped["Event"] = relationship(
        back_populates="predictions", lazy="selectin"
    )
