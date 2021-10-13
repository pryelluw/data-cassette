from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class BaseTape:
    value: Any
    label: str

    def __post_init__(self):
        self.value = self.validate()

    def __call__(self) -> Any:
        return self.value

    def validate(self) -> Any:
        raise NotImplementedError


class StringTape(BaseTape):
    value: str


class IntegerTape(BaseTape):
    value: int


class BooleanTape(BaseTape):
    value: bool


class FloatTape(BaseTape):
    value: float


class ListTape(BaseTape):
    value: list[Any]


class DictTape(Basetape):
    value = Dict[Any, Any]
