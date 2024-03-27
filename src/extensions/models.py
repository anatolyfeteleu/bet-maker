import datetime

from sqlalchemy import TIMESTAMP, BigInteger
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func


class BaseModelMixin(object):
    id: Mapped[int] = mapped_column(
        BigInteger, autoincrement=True, primary_key=True
    )

    created: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        info={"verbose_name": "created"},
    )
    modified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        info={"verbose_name": "modified"},
    )
