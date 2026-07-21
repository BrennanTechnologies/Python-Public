# class Student:
# 	marks = 88
# 	name = 'Sheeran'
# person = Student()

# name = getattr(person, 'name')
# print(name)

# marks = getattr(person, 'marks')
# print(marks)

# Output: Sheeran
#         88

#############################


marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# for iter in iterator_marks:
# 	print(iter)
# exit()

# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)

# Output: 65
#         71