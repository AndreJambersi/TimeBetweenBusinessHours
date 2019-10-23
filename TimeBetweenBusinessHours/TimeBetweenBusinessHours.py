import datetime

class TimeBetweenBusinessHours:

    def __init__(self,datetime_1,datetime_2,work_timing,weekends,holidays_list):
        self.datetime_1 = datetime_1
        self.datetime_2 = datetime_2
        self.work_timing = work_timing
        self.weekends = weekends
        self.holidays_list = holidays_list

    def get_days(self):
        first_day = self.datetime_1
        days = 1
        if((first_day.hour> self.work_timing[1] - 1) or (self.datetime_2.hour< self.work_timing[0])):
            days = days - 1
        while((first_day.day < self.datetime_2.day) or (first_day.month < self.datetime_2.month) or (first_day.year < self.datetime_2.year)):
            if((first_day.isoweekday() not in self.weekends) and (first_day.strftime("%Y-%m-%d") not in self.holidays_list)):
                days += 1
            first_day += datetime.timedelta(days=1)
        return days

    def get_hours(self):
        if(self.datetime_1 > self.datetime_2):
            hours = 0
        elif((self.datetime_1.day == self.datetime_2.day) and (self.datetime_1.month == self.datetime_2.month) and (self.datetime_1.year == self.datetime_2.year)):
            if(self.datetime_1.hour < self.work_timing[0]): #This calculate working hours in the first day
                hours_first_day = self.work_timing[0]
            elif(self.datetime_1.hour > (self.work_timing[1] - 1)):
                hours_first_day = self.work_timing[1]
            else:
                hours_first_day = self.datetime_1.hour
            if(self.datetime_2.hour > self.work_timing[1] - 1): #This calculate working hours in the last day
                hours_last_day = self.work_timing[1]
            elif(self.datetime_2.hour < self.work_timing[0]):
                hours_last_day = self.work_timing[0]
            else:
                hours_last_day = self.datetime_2.hour
            hours = hours_last_day - hours_first_day
        else:
            first_day = self.datetime_1
            days = 1
            hours_day = self.work_timing[1] - self.work_timing[0]
            while((first_day.day < self.datetime_2.day) or (first_day.month < self.datetime_2.month) or (first_day.year < self.datetime_2.year)):
                if((first_day.isoweekday() not in self.weekends) and (first_day.strftime("%Y-%m-%d") not in self.holidays_list)):
                    days += 1
                first_day += datetime.timedelta(days=1)
            if(self.datetime_1.hour < self.work_timing[0]): #This calculate working hours in the first day
                hours_first_day = hours_day
            elif(self.datetime_1.hour > (self.work_timing[1] - 1)):
                hours_first_day = 0
            else:
                hours_first_day = self.work_timing[1] - self.datetime_1.hour
            if(self.datetime_2.hour > self.work_timing[1] - 1): #This calculate working hours in the last day
                hours_last_day = hours_day
            elif(self.datetime_2.hour < self.work_timing[0]):
                hours_last_day = 0
            else:
                hours_last_day = self.datetime_2.hour - self.work_timing[0]
            if(days > 1):
                days = days - 2 #The day function is rounded up, so this ignore the last and first day
                hours = days * hours_day
                hours = hours + hours_last_day + hours_first_day
            else:
                hours = hours_first_day - hours_last_day
        return hours

    def get_hours_and_minutes(self):
        if(self.datetime_1 > self.datetime_2):
            minutes = 0
            hours = 0
        else:
            hours = 0
            if((self.datetime_1.hour < self.work_timing[0]) or
               (self.datetime_1.hour > (self.work_timing[1] - 1))):
                minute_1 = 0
            elif((self.datetime_1.isoweekday() in self.weekends) or
                 (self.datetime_1.strftime("%Y-%m-%d") in self.holidays_list)):
               minute_1 = 0
            else:
                minute_1 = self.datetime_1.minute
            if((self.datetime_2.hour < self.work_timing[0]) or
               (self.datetime_2.hour > (self.work_timing[1] - 1))):
                minute_2 = 0
            elif((self.datetime_2.isoweekday() in self.weekends) or
                 (self.datetime_2.strftime("%Y-%m-%d") in self.holidays_list)):
               minute_2 = 0
            else:
                minute_2 = self.datetime_2.minute
            if(minute_1 < minute_2):
                minutes = minute_2 - minute_1
            elif(minute_1 > minute_2):
                minutes = 60 + minute_2 - minute_1
                hours -= 1
            else:
                minutes = 0
            #Generate hours
            days = 0
            if((self.datetime_1.hour < self.work_timing[0]) or
               (self.datetime_1.hour > (self.work_timing[1] - 1))):
                hours_1 = self.datetime_1.replace(hour=self.work_timing[0],minute=0,second=0).hour
            elif((self.datetime_1.isoweekday() in self.weekends) or
                 (self.datetime_1.strftime("%Y-%m-%d") in self.holidays_list)):
               hours_1 = self.datetime_1.replace(hour=self.work_timing[0],minute=0,second=0).hour
               if(self.datetime_2.hour > (self.work_timing[1] - 1)):
                   days += 1
            else:
                hours_1 = self.datetime_1.hour
            if((self.datetime_2.hour < self.work_timing[0]) or
               (self.datetime_2.hour > (self.work_timing[1] - 1))):
                hours_2 = self.datetime_2.replace(hour=self.work_timing[0],minute=0,second=0).hour
            elif((self.datetime_2.isoweekday() in self.weekends) or
                 (self.datetime_2.strftime("%Y-%m-%d") in self.holidays_list)):
               hours_2 = self.datetime_2.replace(hour=self.work_timing[0],minute=0,second=0).hour
            else:
                hours_2 = self.datetime_2.hour
            first_day = self.datetime_1
            while((first_day.day < self.datetime_2.day) or
                  (first_day.month < self.datetime_2.month) or
                  (first_day.year < self.datetime_2.year)):
                if((first_day.isoweekday() not in self.weekends) and
                   (first_day.strftime("%Y-%m-%d") not in self.holidays_list)):
                    days += 1
                first_day += datetime.timedelta(days=1)
            hours_day = self.work_timing[1] - self.work_timing[0]
            hours = days * hours_day + hours_2 - hours_1 + hours
            if((self.datetime_1.day == self.datetime_2.day) and
               (self.datetime_1.month == self.datetime_2.month) and
               (self.datetime_1.year == self.datetime_2.year)):
                if(self.datetime_1.hour < self.work_timing[0]):
                    hours_1 = self.work_timing[0]
                elif(self.datetime_1.hour > (self.work_timing[1] - 1)):
                    hours_1 = self.work_timing[1]
                else:
                    hours_1 = self.datetime_1.hour
                if(self.datetime_2.hour > self.work_timing[1] - 1):
                    hours_2 = self.work_timing[1]
                elif(self.datetime_2.hour < self.work_timing[0]):
                    hours_2 = self.work_timing[0]
                else:
                    hours_2 = self.datetime_2.hour
                hours = hours_2 - hours_1 + hours
        return str(hours) + ':' + (('0' + str(minutes)) if (len(str(minutes)) == 1) else str(minutes))
