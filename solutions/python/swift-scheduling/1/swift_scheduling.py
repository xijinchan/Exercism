import time

def delivery_date(start, description):
    date = start[0:10]
    time_str = start[11:19]
    hour_int = int(time_str[:2])
    output = ""

    time_tuple = time.strptime(start, "%Y-%m-%dT%H:%M:%S")
    day_of_week = time_tuple.tm_wday
    month = time_tuple.tm_mon
    time_seconds = time.mktime(time_tuple)

    if description == "NOW":
        output_seconds = time_seconds + 7200
        output_tuple = time.gmtime(output_seconds)
        output = time.strftime("%Y-%m-%dT%H:%M:%S", output_tuple)
    elif description == "ASAP" and hour_int < 13:
        output = start[:11] + "17:00:00"
    elif description == "ASAP":
        output_seconds = time_seconds + 86400
        output_tuple = time.gmtime(output_seconds)
        output = time.strftime("%Y-%m-%dT%H:%M:%S", output_tuple)
        output = output[:11] + "13:00:00"
    elif description == "EOW":
        if day_of_week < 3:
            add_seconds = (4 - day_of_week) * 86400
            output_seconds = time_seconds + add_seconds
            output_tuple = time.gmtime(output_seconds)
            output = time.strftime("%Y-%m-%dT%H:%M:%S", output_tuple)
            output = output[:11] + "17:00:00"
        else:
            add_seconds = (6 - day_of_week) * 86400
            output_seconds = time_seconds + add_seconds
            output_tuple = time.gmtime(output_seconds)
            output = time.strftime("%Y-%m-%dT%H:%M:%S", output_tuple)
            output = output[:11] + "20:00:00"
    elif description[-1] == "M":
        Nth = description[:-1]
        if month < int(Nth):
            output = start[:5] + ("0" * (2 - len(Nth))) + Nth + "-01T08:00:00"
            output_tuple = time.strptime(output, "%Y-%m-%dT%H:%M:%S")
            output_day_of_week = output_tuple.tm_wday
            output_day = output_tuple.tm_mday
            if output_day_of_week > 4:
                output_day = output_day + (7 - output_day_of_week)
            output = start[:5] + ("0" * (2 - len(Nth))) + Nth + "-0" + str(output_day) + "T08:00:00"
        elif month >= int(Nth):
            year = start[:4]
            year_next = str(int(year) + 1)
            output = year_next + "-" + ("0" * (2 - len(Nth))) + Nth + "-01T08:00:00" 
            output_tuple = time.strptime(output, "%Y-%m-%dT%H:%M:%S")
            output_day_of_week = output_tuple.tm_wday
            output_day = output_tuple.tm_mday
            if output_day_of_week > 4:
                output_day = output_day + (7 - output_day_of_week)
                output = year_next + "-" + ("0" * (2 - len(Nth))) + Nth + "-0" + str(output_day) + "T08:00:00"
    elif description[0] == "Q":
        Q = description[1]
        current_Q = 0
        Q_last_month_last_day = ""
        if month / 3 <= 1:
            current_Q = 1
        elif month / 3 <= 2:
            current_Q = 2
        elif month / 3 <= 3:
            current_Q = 3
        elif month / 3 <= 4:
            current_Q = 4
        if Q == "1": Q_last_month_last_day = "03-31"
        if Q == "2": Q_last_month_last_day = "06-30"
        if Q == "3": Q_last_month_last_day = "09-30"
        if Q == "4": Q_last_month_last_day = "12-31"
        if int(Q) >= current_Q: 
            output = start[:5] + Q_last_month_last_day + "T08:00:00"
        else:
            year = start[:4]
            year_next = str(int(year) + 1) + "-"
            output = year_next + Q_last_month_last_day + "T08:00:00"
        output_tuple = time.strptime(output, "%Y-%m-%dT%H:%M:%S")
        output_day_of_week = output_tuple.tm_wday
        output_day = output_tuple.tm_mday
        if output_day_of_week > 4:
            output_day = output_day - (output_day_of_week - 4)
            output = output[:8] + str(output_day) + "T08:00:00"

    return output
