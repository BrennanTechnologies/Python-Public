# Python program to explain time.gmtime() method 
  
# importing time module 
import time 

# Time in seconds 
# since the epoch 
#secs = 40000

# Convert the given time in seconds 
# since the epoch to a 
# time.struct_time object in UTC 
# using time.gmtime() method 
obj = time.gmtime() 

# Print the time.struct_time object 
#print("time.struct_time object for seconds =", secs) 
print(obj) 

import CB_Module as cb
cb.lazygit()

exit()

# Time in seconds 
# since the epoch 
secs = 40000.7856
  
# Convert the given time in seconds 
# since the epoch to a 
# time.struct_time object in UTC 
# using time.gmtime() method 
obj = time.gmtime(secs) 
  
# Print the time.struct_time object 
print("\ntime.struct_time object for seconds =", secs) 
print(obj) 