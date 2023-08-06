from collections.abc import MutableMapping
from typing import NamedTuple


class DDCoordinates(NamedTuple):
    long: float
    lat: float

    def to_json(self) -> MutableMapping:
        return {"long": self.long, "lat": self.lat}
