import time

reminder = input("What do you wish to be reminded of?")
time_interval = float(input("how often do you wish to be reminded?(in minutes)"))
time_interval *= 60
time.sleep(time_interval)
print(reminder)
