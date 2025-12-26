import time
'''
The epoch is the point where the time starts, the return value of time.gmtime(0). 

It is January 1, 1970, 00:00:00 (UTC) on all platforms.

'''

nano_time = time.time_ns()
print("nano_time: " + str(nano_time)) # 1,707,001,399,183,015,600

t = time.gmtime(0)
print(t)


