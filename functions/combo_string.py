def combo_string(a, b):
	lenA = len(a)
	lenB = len(b)
	if lenA < lenB:
		str = a + b + a
	else:
		str = b + a + b
	print(str)

combo_string('Hello', 'hi') # 'hiHellohi'
combo_string('hi', 'Hello') # 'hiHellohi'

def combo_string2(a, b):
    if len(a) < len(b):
        print(a + b + a)
    else:
        print(b + a + b)
        
def combo_string3(a, b):
    print(f"{a}{b}{a}" if len(a) < len(b) else f"{b}{a}{b}")