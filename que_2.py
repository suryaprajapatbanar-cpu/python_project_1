students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    print(name,round(avg,2))
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    if avg >=85:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=50:
        grade="C"
    else:
        grade="F"
    print(name,round(avg,2),grade)  
topper=""
highest=0
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    if avg>highest:
        highest=avg 
        topper= name
print("topper : ",topper) 
while True:
    print("1.add student")
    print("2.view all") 
    print("3.show topper")
    print("4.exit")
    ch=int(input("enter choice="))
    if ch==1:
        add_name=input("enter name")
        if add_name in students:
            print("name already exist")
            continue
        marks=[]
        for i in range(3):
            while True:
                mark=int(input("enter marks"))
                if mark >=0 and mark <=100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark, try again.")
        students[add_name]=marks
        print("added succussfully")
    if ch == 2:
        for name,marks in students.items():
            avg=sum(marks)/len(marks)
            if avg >=85:
                grade="A"
            elif avg>+70:
                grade="B"
            elif avg>=50:
                grade="C"
            else:
                grade="F"
            print(name,round(avg,2),grade)
    if ch==3:
        topper=""
        highest=0
        for name,marks in students.items():
            avg=sum(marks)/len(marks)
            if avg>highest:
                highest=avg 
                topper= name
        print("Topper : ",topper)
    if ch==4:
        print("Goodbye!")
        break
    else:
        print("invalid choice")
        break