def func1(*args):
	sum = 0
	for i in args:
		sum = sum + i
	print(sum)

func1(20, 40, 60)
func1(2, 6)

def func2(**kwargs):
	sum = 0
	for subj in kwargs:
		subj_name = subj
		subj_grade = kwargs[subj]
		sum = sum + subj_grade
		print(subj_name + ": " + str(subj_grade))

	ave = sum / len(kwargs)
	print("Ave: " + str(ave))

func2(math=20, science=40, english=60)
