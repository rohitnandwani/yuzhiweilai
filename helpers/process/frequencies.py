from datetime import date, datetime, timedelta


def timePeriodsGenerator(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

def createTimePeriods(start, end, intervalType, intervalValue):
    delta = timedelta(**{intervalType: intervalValue})
    timePeriods = list(timePeriodsGenerator(start, end, delta))
    return timePeriods
