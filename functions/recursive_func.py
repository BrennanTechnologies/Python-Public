def addition(num):
    if num:
        # call same function by reducing number by 1
        print("num: " + str(num))
        return num + addition(num - 1)
    else:
        print("else: " + str(num))
        return 0

res = addition(10)
print(res)
