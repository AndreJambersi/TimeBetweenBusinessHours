def get_days(datetime_1,datetime_2,work_timing,weekends,holidays_list): # Here a datetime without full work time still is count as a day
    first_day = datetime_1
    days = 1
    while(first_day.day < datetime_2.day):
        if((first_day.isoweekday() not in weekends) and (first_day.strftime("%Y-%m-%d") not in holidays_list)):
            days += 1
        first_day += datetime.timedelta(days=1)
    return days

def get_hours(datetime_1,datetime_2,work_timing,weekends,holidays_list): #Round up
    if(datetime_1 > datetime_2):
        hours = 0
    else:
        days = get_days(datetime_1,datetime_2,work_timing,weekends,holidays_list)
        if(days > 1):
            days = days - 2 #The day function is rounded up, so this ignore the last and first day
            hours_day = work_timing[1] - work_timing[0]
            hours = days * hours_day
            if(datetime_1.hour < work_timing[0]): #This calculate working hours in the first day
                hours_first_day = hours_day;
            elif(datetime_1.hour > work_timing[1]):
                hours_first_day = 0
            else:
                hours_first_day = work_timing[1] - datetime_1.hour
            if(datetime_2.hour > work_timing[1]): #This calculate working hours in the last day
                hours_last_day = hours_day;
            elif(datetime_2.hour < work_timing[0]):
                hours_last_day = 0
            else:
                hours_last_day = datetime_2.hour - work_timing[0]
            hours = hours + hours_first_day + hours_last_day
        else:
            hours = datetime_1.hour - datetime_2.hour #days minimum value is suposed to be 1
    return hours

def get_hours_and_minutes(datetime_1,datetime_2,work_timing,weekends,holidays_list):
    if(datetime_1 > datetime_2):
        minutes = 0
        hours = 0
    else:
        if((datetime_1.hour < work_timing[0]) or (datetime_1.hour > work_timing[1])):
            minute_1 = 0
        else:
            minute_1 = datetime_1.minute
        if((datetime_2.hour < work_timing[0]) or (datetime_2.hour > work_timing[1])):
            minute_2 = 0
        else:
            minute_2 = datetime_2.minute
        if(minute_1 < minute_2):
            minutes = minute_2 - minute_1
        elif(minute_1 > minute_2):
            minutes = 60 + minute_2 - minute_1
        else:
            minutes = 0
        if((datetime_1.hour < work_timing[0]) or (datetime_1.hour > work_timing[1])):
            hours_1 = 0
        else:
            hours_1 = datetime_1.hour
        if((datetime_2.hour < work_timing[0]) or (datetime_2.hour > work_timing[1])):
            hours_2 = 0
        else:
            hours_2 = datetime_2.hour
  #Generate hours
        days = get_days(datetime_1,datetime_2,work_timing,weekends,holidays_list)
        if(days > 1):
            days = days - 2
            hours_day = work_timing[1] - work_timing[0]
            hours = days * hours_day + hours_2 + (8 - hours_1)
        else:
            if(hours_1 < hours_2):
                hours = hours_2 - hours_1
            elif(hours_1 > hours_2):
                hours = 8 + hours_2 - hours_1
            else:
                hours = 0
    return str(hours) + ':' + str(minutes)
