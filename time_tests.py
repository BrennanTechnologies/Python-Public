'''
	The epoch is the point where the time starts, the return value of time.gmtime(0). 
	It is January 1, 1970, 00:00:00 (UTC) on all platforms.

'''

import time
'''
The epoch is the point where the time starts, the return value of time.gmtime(0). 

It is January 1, 1970, 00:00:00 (UTC) on all platforms.

'''

### time.time() returns the current time in seconds since the epoch.
t = time.time()
print("t: " + str(t))
t_secs = t

# time.time_ns() returns the current time in nanoseconds since the epoch.
n_t = time.time_ns()
print("n_t: " + str(n_t))
n_secs = n_t

# Convert Secs to Current Date
# ------------------------------
t_yrs = t_secs/60/60/24/365.25
n_yrs = n_secs/1000000000/60/60/24/365.25
print("t_yrs" + str(t_yrs))
print("n_yrs: " + str(n_yrs))

# 1706977037853296200
# 1706976645.4019806




#current_epoch_time = time.gmtime(0)
#print(current_epoch_time)
