str = "HiHo Highlights"
count = 0
for i in range(len(str)):
	str = str.lower()
	sub = str[i:i+2]
	if sub == "HI".lower():
		count +=1
	print(sub)
print(count)
