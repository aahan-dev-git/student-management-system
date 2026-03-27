from student import Student

class Manager:
    def __init__(self):
        self.students = []
        self.load_students()

    def add_students(self,student):
        with open("file.txt","a") as f:
            f.write(f"{student.roll_no},{student.name},{student.age},{student.marks}\n")
        self.students.append(student)
    def load_students(self):
        with open("file.txt", "r") as f:
            for line in f:
                line = line.strip()
                parts = line.split(",")

                roll_no = int(parts[0])
                name = parts[1]
                age = int(parts[2])
                marks = int(parts[3])

                student = Student(name,age,marks,roll_no)
                self.students.append(student)
    def display_students(self):
        for s in self.students:
            print(s)
    def search_student(self):
        roll_input = int(input("enter roll no : "))
        for s in self.students:  
            if roll_input == s.roll_no:
                print(s)
                break
        else:
            print('student not found')
    def update_student(self):
        roll_input = int(input("enter roll number : "))
        for s in self.students:  
            if roll_input == s.roll_no:
                user_inp = input("what do you want to update : ")
                if user_inp == "name":
                    inp = input("enter your name : ")
                    s.name = inp
                    
                    
                elif user_inp == "age":
                    inp_2 = int(input("enter your age : "))
                    s.age = inp_2
                    
                    
                elif user_inp == "marks":
                    inp_3 = int(input("enter your marks : "))
                    s.marks = inp_3
    def update_student(self):
        roll_input = int(input("enter roll number : "))
        for s in self.students:
            if roll_input == s.roll_no:

                while True:
                        inpu = input("what do you want to update : ")
                        if inpu == "name":
                            i = input("enter your name : ")
                            s.name = i
                        
                        
                        elif inpu == "age":
                            inp_2 = int(input("enter your age : "))
                            s.age = inp_2
                    
                        
                        
                        elif inpu == "marks":
                            inp_3 = int(input("enter your marks : "))
                            s.marks = inp_3
                            
                        else:
                            print("invalid field")
                        any_als = input("do you want to update anything else : ")
                        if any_als != "yes":
                            break

                return        
        
        print("student not found")
    def add_update(self):
        with open("file.txt", "w") as f:
            for s in self.students:
                f.write(f"{s.roll_no},{s.name},{s.age},{s.marks}\n")
    def delete(self):
        ent_roll = int(input("enter the roll number of the student you want to delete : "))
        for s in self.students:
            if  ent_roll==s.roll_no:
                self.students.remove(s)
                print("removed")
                self.add_update()
                break
        else:
            print("invalid")
            
        
            
                

    

    
    
            
