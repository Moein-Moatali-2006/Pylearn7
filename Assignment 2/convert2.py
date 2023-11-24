#Moein Moatali
""" Convert second """


total_seconds = float(input('Enter a number of seconds: '))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)