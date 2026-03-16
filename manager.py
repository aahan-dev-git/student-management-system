

class Manager:
    def __init__(self):
        self.students = []

    def add_students(self,student):
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
            
