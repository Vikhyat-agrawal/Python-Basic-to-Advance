student=[]
for i in range(6):
    marks=int(input("enter the marks: "))
    student.append(marks)
    student.sort()
print("The sorted marks are: ",student)