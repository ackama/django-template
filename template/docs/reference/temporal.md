# Temporal Utilities

The `{{ project_module }}.utils.temporal` module provides timezone-aware datetime
utilities to prevent common datetime bugs in Django applications.

## Why?

Django best practice is to always use timezone-aware datetimes. Using naive datetimes
(without timezone information) can lead to subtle bugs, especially when handling data
across different timezones or daylight saving time boundaries.

This project enforces timezone-aware datetime usage through linting (DTZ rules). If you
see errors like:

```
DTZ005 `datetime.datetime.now()` called without a `tz` argument
```

**Use the temporal utility instead of standard datetime methods.**

## Common Usage

Replace standard datetime calls with temporal equivalents:

| ❌ Don't use | ✅ Use instead |
|--------------|----------------|
| `datetime.datetime.now()` | `temporal.now()` |
| `datetime.datetime.today()` | `temporal.today()` |
| `datetime.datetime.utcnow()` | `temporal.now()` |
| `datetime.date.today()` | `temporal.today()` |

## Available Functions

### `now() -> datetime`
Returns the current datetime in the timezone set in Django settings (`TIME_ZONE`).

```python
from {{ project_module }}.utils import temporal

current_time = temporal.now()
```

### `today() -> date`
Returns the current date in the system timezone.

```python
current_date = temporal.today()
```

### `yesterday() -> date` / `tomorrow() -> date`
Returns yesterday's or tomorrow's date in the system timezone.

```python
yesterday_date = temporal.yesterday()
tomorrow_date = temporal.tomorrow()
```

### `make_tz_aware(value: date | datetime) -> datetime`
Converts a naive datetime or date to a timezone-aware datetime using the Django
`TIME_ZONE` setting.

```python
naive_dt = datetime.datetime(2026, 4, 30, 12, 0)
aware_dt = temporal.make_tz_aware(naive_dt)
```

### `midnight(dt: date | datetime) -> datetime`
Returns midnight for the given date in the system timezone.

```python
start_of_day = temporal.midnight(temporal.today())
```

### `extract_datetime_from_string(text: str) -> datetime | None`
Attempts to parse a datetime from a string (useful for parsing dates from filenames or
user input).

```python
dt = temporal.extract_datetime_from_string("report_2026-04-30.pdf")
# Returns: datetime(2026, 4, 30, 0, 0, tzinfo=...)
```

### Business Day Utilities

#### `get_weekdays(start: date, num_days: int) -> list[date]`
Returns a list of weekdays (Monday-Friday) starting from a given date.

```python
weekdays = temporal.get_weekdays(temporal.today(), 5)
# Returns next 5 business days
```

#### `get_weekdays_between(start: date, end: date) -> list[date]`
Returns all weekdays between two dates (inclusive).

```python
weekdays = temporal.get_weekdays_between(
    temporal.today(),
    temporal.today() + datetime.timedelta(days=14)
)
```

### Date Ranges

#### `DatetimeRange`
A dataclass for representing datetime ranges with comparison operators.

```python
from {{ project_module }}.utils.temporal import DatetimeRange

range1 = DatetimeRange(
    start=temporal.now(),
    end=temporal.now() + datetime.timedelta(days=7)
)

# Check if a datetime is in the range
if some_datetime in range1:
    print("In range!")

# Compare ranges
range2 = DatetimeRange(start=..., end=...)
if range1 < range2:
    print("Range1 is entirely before range2")

# Get the last day
last_day = range1.last_day
```

## Testing

In tests, use `time-machine` to freeze time:

```python
import time_machine
from {{ project_module }}.utils import temporal

@time_machine.travel("2026-04-30 10:00:00", tick=False)
def test_something():
    assert temporal.now().day == 30
```

## Configuration

The timezone is configured in `settings.py`:

```python
TIME_ZONE = "UTC"
USE_TZ = True
```

All temporal functions respect this setting.
