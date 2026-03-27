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
    
            
