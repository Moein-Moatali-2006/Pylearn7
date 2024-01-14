# class Time [__init__,fix,show,sum_time,subtract_time,convert_time_to_second,convert_second_to_time,GMT_to_Tehran]
class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        self.fix()


    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1
        
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

        if self.hour < 0:
            print('your time is false')

    def show(self):
        print(self.hour,":",self.minute,":",self.second)

    def sum_time(self,other):
        new_second = self.second + other.second
        new_minute = self.minute + other.minute
        new_hour = self.hour + other.hour
        result = Time(new_hour,new_minute,new_second)
        return result
    
    def subtract_time(self,other):
        new_second = self.second - other.second
        new_minute = self.minute - other.minute
        new_hour = self.hour - other.hour
        result = Time(new_hour,new_minute,new_second)
        return result 
    
    def convert_second_to_time(self,second):
        hour = second // 3600
        h = second % 3600
        minute = h // 60
        second = h % 60
        result = Time(hour,minute,second)
        return result
    
    def convert_time_to_second(self,hour,minute,second):
        hour = hour * 3600
        minute = minute * 60
        result = hour + minute + second
        print(result)

    def GMT_to_Tehran(self,hour,minute,second):
        new_hour = hour + 3
        new_minute = minute + 30
        result = Time(new_hour,new_minute,second)
        return result


t1=Time(5,45,15)
t2=Time(4,70,35)
# sum
t3=t1.sum_time(t2).show()
# subtract 
t4=t1.subtract_time(t2).show()
# convert second to time 
t5=t1.convert_second_to_time(3661).show()
# convert time to second 
t6=t1.convert_time_to_second(1,1,1)
# GMT to Tehran
t7=t1.GMT_to_Tehran(5,10,20).show()




