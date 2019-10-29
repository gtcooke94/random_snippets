import datetime
import calendar

def meetup_date(year, month, nth=4, weekday=3):
    if nth > 0:
        # Start from the beginning of the month
        current = datetime.date(year, month, 1)
        current_nth = 1
        advance_day = 1
        advance_week = 7
    else:
        # Start from the end of the month ex: nth = -2, weekday = 3 would be the second to last Thursday of the month
        current = datetime.date(year, month, calendar.monthrange(year, month)[1])
        current_nth = 1
        advance_day = -1
        advance_week = -7
        nth = -nth


    while current.weekday() != weekday:
        current = advance_days(current, advance_day)
    while current_nth != nth:
        current = advance_days(current, advance_week)
        current_nth += 1
    return current

def advance_days(current, days):
    return current + datetime.timedelta(days=days)


