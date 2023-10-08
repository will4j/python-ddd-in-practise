from datetime import datetime

TIME_FMT = "%Y%m%d%H%M%S"


def fmt_current_time() -> str:
    return fmt_time(datetime.now())


def fmt_time(time_obj: datetime) -> str:
    return datetime.strftime(time_obj, TIME_FMT)
