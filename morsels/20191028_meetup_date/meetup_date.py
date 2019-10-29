import datetime
def meetup_date(year, month, nth=4, weekday=3):
    current = datetime.date(year, month, 1)
    current_nth = 1
    while current.weekday() != weekday:
        current = advance_days(current, 1)
    while current_nth != nth:
        current = advance_days(current, 7)
        current_nth += 1
    return current

def advance_days(current, days):
    return current + datetime.timedelta(days=days)


