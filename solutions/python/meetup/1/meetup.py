import datetime

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):    
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index = weekday.index(day_of_week)

    teenths = [13,14,15,16,17,18,19]
    
    if week == 'first':
        first_day = datetime.date(year, month, 1).weekday()
        day = 1 + ((day_index - first_day) % 7)

    if week == 'second':
        first_day = datetime.date(year, month, 1).weekday()
        day = 8 + ((day_index - first_day) % 7)

    if week == 'third':
        first_day = datetime.date(year, month, 1).weekday()
        day = 15 + ((day_index - first_day) % 7)

    if week == 'fourth':
        first_day = datetime.date(year, month, 1).weekday()
        day = 22 + ((day_index - first_day) % 7)

    if week == 'fifth':
        first_day = datetime.date(year, month, 1).weekday()
        day = 29 + ((day_index - first_day) % 7)
        if day > (datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)).day:
            raise MeetupDayException('That day does not exist.')

    if week == 'teenth':
        first_day = datetime.date(year, month, 1).weekday()
        day = [k for k in [(1 + ((day_index - first_day + 7) % 7) + k) for k in range(0,22,7)] if k in teenths][0]

    if week == 'last':
        if month == 12:
            last_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            last_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        last_day = last_date.weekday()
        day = last_date.day - ((last_day - day_index) % 7)

    return datetime.date(year, month, day)
