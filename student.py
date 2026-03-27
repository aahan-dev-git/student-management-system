class Student:
    def __init__(self,name,age,marks,roll_no):
        self.name = name
        self.age = age
        self.marks = marks
        self.roll_no = roll_no
    def __str__(self):
        return f"name:{self.name}\nage:{self.age}\nmarks:{self.marks}\nroll no:{self.roll_no}"