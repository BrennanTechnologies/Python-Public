

value = [1, 2, 3, 4] 
data = 0
data = value[3] 
print(data)
exit()
try: 
    data = value[4] 
except IndexError: 
    print('GFG', end = '') 
except: 
    print('GeeksforGeeks ', end = '') 