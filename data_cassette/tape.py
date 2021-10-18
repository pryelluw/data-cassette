from dataclasses import dataclass
from typing import Tuple, Any
from inspect import signature


@dataclass
class Tape:
    _tracks: list[Tuple[str, Any]]


    def __post_init__(self):
        if type(self._tracks) != list:
            raise TypeError('List of tuples expected')

        for track in self._tracks:
            if type(track) != tuple:
                raise TypeError('Tuple type exptected for track items')

            if type(track[0]) != str:
                raise TypeError('First tuple item must be str type')  

    @property
    def tracks(self):
        return self._tracks
    
    @tracks.setter
    def tracks(self, _):
        raise Exception('Tracks my not be updated')
