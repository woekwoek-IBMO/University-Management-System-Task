class Person:
    def __init__ (self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def set_details(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def get_details (self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student (Person):
    def __init__ (self, name, age, gender, student_ID, course):
        super().__init__(name, age, gender)
        self.student_ID=student_ID
        self.course=course
        self.grades=[]
        self.average=0
    
    def set_student_details (self, student_ID, course):
        self.student_ID = student_ID
        self.course = course
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade (self):
        if self.grades [0] == "":
            pass
        else:
            average= sum(self.grades) / len(self.grades)
            self.average = average
        
    def get_student_summary(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStudent ID: {self.student_ID}\nCourse: {self.course}\nAverage grade: {self.average}")

class Professor (Person):
    def __init__ (self, name, age, gender, staff_ID, department, salary):
        super().__init__(name, age, gender)
        self.staff_ID=staff_ID
        self.department= department
        self.salary = salary

