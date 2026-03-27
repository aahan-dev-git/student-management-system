from student import Student
from manager import Manager
manager = Manager()
choices = ["1.Add Students","2.View Students","3.Search Student","4.Update","5.delete","6.exit"]


while True:
    for i in choices:
        print(i)
    user_choice = int(input("enter choice = "))
    if user_choice == 1:
        name = input("enter name : ")
        age = int(input("enter age : "))
        marks = int(input("enter marks : "))
        roll_no = int(input("enter roll number : "))
        s = Student(name,age,marks,roll_no)
        manager.add_students(s)
    elif user_choice == 2:
        manager.display_students()
    elif user_choice == 3:
        manager.search_student()
    elif user_choice == 4:
        manager.update_student()
        manager.add_update()
    elif user_choice == 5:
        manager.delete()
    elif user_choice == 6:
        exit()
    else:
        print("invalid choice")