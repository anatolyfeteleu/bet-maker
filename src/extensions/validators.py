from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator


def positive_decimal(val: Decimal):
    assert val > 0, "value must be positive"
    return val


def scaled_decimal(val: Decimal):
    assert len(str(val).split(".")) == 2, "use scaled decimal number"
    return val


PositiveDecimal = Annotated[
    Decimal,
    AfterValidator(positive_decimal),
    AfterValidator(scaled_decimal),
]
