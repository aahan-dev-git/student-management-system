class Student:
    def __init__(self,name,age,roll_no,marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks
    def __str__(self):
        return f"name:{self.name}\nage:{self.age}\nmarks:{self.marks}\nroll no:{self.roll_no}"