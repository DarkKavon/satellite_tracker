from src.coordniates.dd_coordinates import DDCoordinates
from typing import NamedTuple


class DMSCoordinate:
    def __init__(self, input):
        input = str(input).split(':')
        self.degrees = int(input[0])
        self.minutes = int(input[1])
        self.seconds = float(input[2])

    def __repr__(self):
        return f"""{self.degrees}° {self.minutes}' {self.seconds}\""""



class DMSCoordinates(NamedTuple):
    long: DMSCoordinate
    lat: DMSCoordinate

    @staticmethod
    def convert_dms_to_dd(input: DMSCoordinate) -> float:
        return input.degrees + input.minutes // 60 + input.minutes / 60 + input.seconds // 360 + input.seconds / 3600

    def convert_to_dd(self) -> DDCoordinates:
        return DDCoordinates(self.convert_dms_to_dd(self.long), self.convert_dms_to_dd(self.lat))