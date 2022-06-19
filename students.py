

students=[]
course=int(input("Please enter your students count? "))
count=0
for i in range(course):
    x=float(input("please enter your programming lesson score: "))
    
    students.append(x)
    sum1=sum(students)

average=sum1/course
print("average is: ",average,"max score: ",max(students),"min score: ",min(students))


