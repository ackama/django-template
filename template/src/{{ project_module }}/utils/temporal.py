import dataclasses
import datetime
import re
import zoneinfo
from collections import abc

from dateutil import parser
from django.conf import settings
from django.utils import timezone


@dataclasses.dataclass
class DatetimeRange:
    start: datetime.datetime
    end: datetime.datetime  # Exclusive

    def __contains__(self, value: datetime.date | datetime.datetime) -> bool:
        value = make_tz_aware(value)
        return self.start <= value < self.end

    def __lt__(self, value: datetime.date | datetime.datetime) -> bool:
        value = make_tz_aware(value)
        return self.end <= value

    def __gt__(self, value: datetime.date | datetime.datetime) -> bool:
        value = make_tz_aware(value)
        return value < self.start

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DatetimeRange):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __len__(self) -> int:
        return (self.end - self.start).days

    def __repr__(self) -> str:
        return f"DatetimeRange(start={self.start}, end={self.end})"

    @property
    def last_day(self) -> datetime.date:
        return (self.end - datetime.timedelta(days=1)).date()


def extract_datetime_from_string(
    file_name: str, delimiters: abc.Iterable[str] = (".", "_")
) -> datetime.datetime:
    """
    Attempt to extract the datetime from a string.

    The string is first split by the delimiters and then each segment is parsed in an
    attempt to find a datetime. The first datetime found is returned.
    """

    split_pattern = re.compile("|".join([re.escape(d) for d in delimiters]))

    tzinfo = zoneinfo.ZoneInfo(settings.TIME_ZONE)

    segments = re.split(split_pattern, file_name)
    file_date: datetime.datetime | None = None
    for segment in segments:
        try:
            file_date = parser.parse(segment, fuzzy=False)
            return file_date.replace(tzinfo=tzinfo)
        except parser.ParserError, OverflowError:
            pass

    raise ValueError(f"Could not extract datetime from filename '{file_name}'")


def make_tz_aware(value: datetime.datetime | datetime.date) -> datetime.datetime:
    """
    Return a TZ-aware datetime of the passed date/datetime.
    """
    tzinfo = zoneinfo.ZoneInfo(settings.TIME_ZONE)
    if isinstance(value, datetime.datetime):
        dt = value
    else:
        dt = datetime.datetime.combine(value, datetime.time(0))

    if timezone.is_naive(dt):
        return timezone.make_aware(dt, timezone=tzinfo)
    return dt.astimezone(tzinfo)


def now() -> datetime.datetime:
    """
    Return now in system timezone
    """
    tzinfo = zoneinfo.ZoneInfo(settings.TIME_ZONE)
    return timezone.now().astimezone(tzinfo)


def today() -> datetime.date:
    """
    Return today in system timezone
    """
    return now().date()


def yesterday() -> datetime.date:
    """
    Return yesterday in system timezone
    """
    return now().date() - datetime.timedelta(days=1)


def tomorrow() -> datetime.date:
    """
    Return tomorrow in system timezone
    """
    return now().date() + datetime.timedelta(days=1)


def midnight(
    value: datetime.datetime | datetime.date | None = None,
) -> datetime.datetime:
    """
    Return midnight in system timezone
    """
    tzinfo = zoneinfo.ZoneInfo(settings.TIME_ZONE)

    if value is None:
        value = timezone.now()
    elif isinstance(value, datetime.date):
        value = datetime.datetime.combine(value, datetime.time(0))

    if timezone.is_naive(value):
        value = timezone.make_aware(value, timezone=tzinfo)
    else:
        value = value.astimezone(tzinfo)

    return value.replace(hour=0, minute=0, second=0, microsecond=0)


def get_weekdays(period: DatetimeRange) -> int:
    """
    Calculate the number of weekdays in a period.

    Note that the period start date is inclusive and the end is exclusive.
    """
    start_date = period.start.date()
    end_date = period.end.date()

    total_days = (end_date - start_date).days
    full_weeks, extra_days = divmod(total_days, 7)

    weekdays = full_weeks * 5

    # Handle remaining days
    for i in range(extra_days):
        if (start_date + datetime.timedelta(days=i)).weekday() < 5:
            weekdays += 1

    return weekdays


def get_weekdays_between(
    start: datetime.date | datetime.datetime, end: datetime.date | datetime.datetime
) -> int:
    """
    Calculate the number of weekdays between 2 dates.

    Note that the start is inclusive and the end is exclusive.
    """
    start_date = make_tz_aware(start)
    end_date = make_tz_aware(end)
    return get_weekdays(DatetimeRange(start_date, end_date))
