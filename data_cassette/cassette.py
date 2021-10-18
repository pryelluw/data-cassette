from dataclasses import dataclass
from typing import Tuple, Any
from inspect import signature
from tape import Tape

@dataclass
class Cassette:
    _tape: Tape
    _title: str
    _description: str

    def __post_init__(self):
        if type(self._Tape) != Tape:
            raise TypeError('<class \'Tape\'>  expected')
        
        elif type(self._title) != str:
            raise TypeError('str type expected')
        
        elif type(self._description) != str:
            raise TypeError('str type expected')
    
        elif len(self._title) <= 0:
            raise Exception('Title may not be empty string')
        
        elif len(self._description) <= 0:
            raise Exception('Descriptiopn may not be empty string')

    @property
    def tape(self):
        return self._tape
    
    @tape.setter
    def tape(self, _):
        raise Exception('Tape may not be updated')
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, _):
        raise Exception('Title may not be updated')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, _):
        raise Exception('Description may not be updated')