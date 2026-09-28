import time
current_time = time.localtime()
hour = current_time.tm_hour
if(hour<12):
    print("Good Morning: ")
elif(hour<17):
    print("Good AfterNoon: ")
else:
    print("Good Evening: ")
