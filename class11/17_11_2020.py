limit=int(input("Enter the no of Students"))
student_names=list()
student_marks=list()
student_details=dict()
j=0
for i in range(0,limit):
    print("Enter the Name of Student ",i)
    name = input()
    student_names.append(name)
    print("Enter the Marks of ", name)
    marks = int(input())
    student_marks.append(marks)

print(student_names)
print(student_marks)

for i in student_names:
    student_details[i]=student_marks[j]
    j=j+1

print(student_details)