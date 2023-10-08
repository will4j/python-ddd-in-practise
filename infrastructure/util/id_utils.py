import shortuuid

from infrastructure.util import time_utils


def timed_uuid(namespace: str) -> str:
    return f"{namespace}-{time_utils.fmt_current_time()}-{shortuuid.random(length=8).lower()}"
