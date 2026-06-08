class Student:
    def __init__(self,name,student_no,course):
        self.name=name
        self.course=course
        self.student_no=student_no
    def study(self):
        print(f"{self.name} studies")
    def eat(self):
        print(f"{self.name} eats")
    def get_details(self):
        print("userdetails")
        print(f"Name:{self.name}-Student No:{self.student_no}-Course:{self.course}")

student1 = Student('Abby','C027','BBIT')
print(student1.name)
print(student1.course)
print(student1.student_no)

student2= Student('Jane','C028','BIT')
print(student2.name)
print(student2.course)
print(student2.student_no)
student1.study()
student1.eat()
student1.get_details()
