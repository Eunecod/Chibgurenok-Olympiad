from datetime import datetime, timezone


def CurrentTimestamp() -> int:
    return int(datetime.now(timezone.utc).astimezone(datetime.now().utcoffset()).timestamp())


def CurrentDatestamp() -> int:
    return FormatDatestamp(datetime.now(timezone.utc).astimezone(datetime.now().utcoffset()).date().isoformat())


def FormatDatestamp(sDate: str) -> int:
    return int(sDate.replace('-', ''))
