from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class BaseTrack:
    value: Any
    label: str

    def __post_init__(self):
        self.value = self.validate()

    def __call__(self) -> Any:
        return self.value

    def validate(self) -> Any:
        raise NotImplementedError


class StringTrack(BaseTrack):
    value: str


class IntegerTrack(BaseTrack):
    value: int


class BooleanTrack(BaseTrack):
    value: bool


class FloatTrack(BaseTrack):
    value: float


class ListTrack(BaseTrack):
    value: list[Any]


class DictTrack(BaseTrack):
    value = Dict[Any, Any]
