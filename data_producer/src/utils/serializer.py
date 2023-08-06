import json
from collections.abc import MutableMapping


def serializer(data: MutableMapping) -> str:
    return json.dumps(data).encode("utf-8")
