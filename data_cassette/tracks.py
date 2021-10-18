from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class BaseTrack:
    _label: str
    _value: Any
    

    def __post_init__(self):
        if type(self._label) != str:
            raise TypeError('str type expected for label')

        self._value = self.validate()

    def __call__(self) -> Any:
        return self.value

    def validate(self) -> Any:
        '''
        Validate track value
        Docstring required for documentation
        '''
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
