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
            self.average = round(average,0)
        
    def get_student_summary(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStudent ID: {self.student_ID}\nCourse: {self.course}\nAverage grade: {self.average}")

class Professor (Person):
    def __init__ (self, name, age, gender, staff_ID, department, salary):
        super().__init__(name, age, gender)
        self.staff_ID = staff_ID
        self.department = department
        self.salary = salary

    def set_professor_details (self, staff_ID, department, salary):
        self.staff_ID = staff_ID
        self.department = department
        self.salary = salary

    def give_feedback(self, Student, feedback):
        print(f"Feedback for {Student.name}: {feedback}")
    
    def increase_salary (self, percentage):
        self.salary += (percentage/100)*self.salary

    def mentor_student(self, Student):
        print(f"Professor {self.name} is now mentoring student {Student.name} on {Student.course}")
    
    def get_professor_summary(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStaff ID: {self.staff_ID}\nDepartment: {self.department}\nSalary: {self.salary}")
    

class Administrator (Person):
    def __init__ (self, name, age, gender, admin_ID, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_ID = admin_ID
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, admin_ID, office, years_of_service):
        self.admin_ID = admin_ID
        self.office = office
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service +=1
    
    def get_admin_summary (self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAdmin ID: {self.admin_ID}\nOffice: {self.office}\nYears of service: {self.years_of_service}")


Student1= Student("Ibrahim", 17, "Male", "S5678", "Computer Science")
Student2 = Student("Maryam", 16, "Female", "S1234", "History")

Professor1=Professor("Miss Odell", 56, "Female", "P5678", "Geography", 55000)
Professor2 = Professor("Mr Cole", 28, "Male", "P1234", "History", 49500)

Administrator1= Administrator("Mr Reed", 50, "Male", "A2345", "Room 12, Admin block", 20)

Student1.add_grade(9)
Student1.add_grade(8)
Student1.add_grade(9)
Student1.add_grade(9)
Student1.add_grade(8)
Student1.add_grade(7)

Student1.calculate_average_grade()

Professor1.give_feedback(Student1,"Well done on passing your test!")
Professor2.increase_salary(10)

Administrator1.increment_service_years()

Student1.get_student_summary()
Student2.get_student_summary()
Professor1.get_professor_summary()
Professor2.get_professor_summary()
Administrator1.get_admin_summary()

Professor2.mentor_student(Student2)