import time as t

t.localtime()

time_now = t.localtime()

#tm.hour and tm.min





print("It is now", str(time_now.tm_hour) + "h" + str(time_now.tm_min)+"m")

print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min)+"m")


# t.sleep(5) this code can be used to put a delay on when code is run, the argument is in
# seconds
