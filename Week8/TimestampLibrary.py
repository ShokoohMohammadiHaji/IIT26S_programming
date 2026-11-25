
from datetime import datetime


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    file = open(PFilename, "r")

    Row = file.readline()

    while Row != "":
        Row = Row.strip()

        if Row != "":
            Timestamp = datetime.strptime(Row, "%Y-%m-%dT%H:%M")
            PTimestamps.append(Timestamp)

        Row = file.readline()

    file.close()
    return None


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    amount = 0

    for Timestamp in PTimestamps:
        if Timestamp.year == PYear:
            amount += 1

    return amount


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    amount = 0

    for Timestamp in PTimestamps:
        if MONTHS[Timestamp.month - 1] == PMonth:
            amount += 1

    return amount


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    amount = 0

    for Timestamp in PTimestamps:
        if WEEKDAYS[Timestamp.weekday()] == PWeekday:
            amount += 1

    return amount
