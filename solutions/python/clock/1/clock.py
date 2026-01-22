class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return 'Clock' + str((self.hour, self.minute))

    def __str__(self):
        hour_edited = self.hour
        minute_edited = self.minute

        if minute_edited > 59 or minute_edited < 0:
            minute_edited = minute_edited % 60
            hour_edited += int((self.minute / 60) // 1)
        if hour_edited > 23 or hour_edited < 0:
            hour_edited = hour_edited % 24
            
        return ((('0' + str(hour_edited)) if hour_edited < 10 else str(hour_edited)) + ':' + (('0' + str(minute_edited)) if minute_edited < 10 else str(minute_edited)))

    def __eq__(self, other):
        return bool(str(self) == str(other))

    def __add__(self, minutes):
        self.minute += minutes
        return str(self)
        
    def __sub__(self, minutes):
        self.minute -= minutes
        return str(self)
