## **Project: University Management System**

### **Objective**  
Design a system for managing a UK university’s staff and students. You will use classes with shared attributes and methods, inheritance, and composition to simulate interactions between objects.

---

### **Step 1: Define the Base Class**

### **1. Person Class**  
A general class for all individuals at the university.  

**Attributes**:  
- `name`: The full name of the person.  
- `age`: The age of the person.  
- `gender`: The gender of the person.  

**Methods**:  
- `set_details(name, age, gender)`: Sets the person's details.  
- `get_details()`: Returns the person's details in the format:  
  `"Name: [name], Age: [age], Gender: [gender]"`.  

---

### **Step 2: Define Subclasses**

### **2. Student Class (inherits from Person)**  
A class for students at the university.  

**Attributes**:  
- Inherits all attributes from `Person`.  
- `student_id`: The student’s unique ID (e.g., "S1234").  
- `course`: The course the student is studying (e.g., "Economics").  
- `grades`: A list of grades (initially empty).  

**Methods**:  
- `set_student_details(student_id, course)`: Sets the student's unique ID and course.  
- `add_grade(grade)`: Adds a grade to the student's list of grades.  
- `calculate_average_grade()`: Calculates and returns the average grade if there are grades, otherwise returns 0.  
- `get_student_summary()`: Returns a summary of the student's details including their average grade.  

---

### **3. Professor Class (inherits from Person)**  
A class for professors at the university.  

**Attributes**:  
- Inherits all attributes from `Person`.  
- `staff_id`: The professor's unique staff ID (e.g., "P5678").  
- `department`: The department the professor belongs to (e.g., "History").  
- `salary`: The annual salary of the professor.  

**Methods**:  
- `set_professor_details(staff_id, department, salary)`: Sets the professor's unique ID, department, and salary.  
- `give_feedback(student, feedback)`: Accepts a `Student` object and a feedback string, then prints:  
  `"Feedback for [student_name]: [feedback]"`.  
- `increase_salary(percentage)`: Increases the professor's salary by the given percentage.  
- `get_professor_summary()`: Returns a summary of the professor's details including their salary.  

**Example for Composition**:  
Here’s how the `give_feedback` method demonstrates composition:  

```python
# Example
professor = Professor()
professor.set_details("Dr. Smith", 45, "Male")
professor.set_professor_details("P1234", "Mathematics", 55000)

student = Student()
student.set_details("Alice Johnson", 20, "Female")
student.set_student_details("S5678", "Physics")

professor.give_feedback(student, "Great work on your assignment!")
# Output: Feedback for Alice Johnson: Great work on your assignment!
```

---

### **4. Administrator Class (inherits from Person)**  
A class for university administrators.  

**Attributes**:  
- Inherits all attributes from `Person`.  
- `admin_id`: The administrator's unique ID (e.g., "A4321").  
- `office`: The administrator's office location (e.g., "Room 12, Admin Block").  
- `years_of_service`: The number of years the administrator has worked at the university.  

**Methods**:  
- `set_admin_details(admin_id, office, years_of_service)`: Sets the administrator's unique ID, office, and years of service.  
- `increment_service_years()`: Increases the `years_of_service` by 1.  
- `get_admin_summary()`: Returns a summary of the administrator's details including their years of service.  

---

### **Step 3: Create and Use the Classes**

1. **Create Objects**  
   - Create 2 `Student` objects.  
   - Create 2 `Professor` objects.  
   - Create 1 `Administrator` object.  

2. **Demonstrate Functionality**  
   - Add grades to a student and calculate their average grade.  
   - Use a professor to give feedback to a student.  
   - Increase a professor's salary by 10%.  
   - Increment an administrator's years of service.  

3. **Output**  
   - Print the summaries of all objects to show updated details.  

---

### **Extension Task (Harder)**

**Scenario**: Implement a mentoring relationship between a professor and a student.

1. Add a `mentor_student(student)` method to the `Professor` class that accepts a `Student` object. This method should:  
   - Print a message in the format:  
     `"Professor [professor_name] is now mentoring Student [student_name] on [student_course]"`.  

2. Add a `get_mentor()` method to the `Student` class that returns the professor's name if the student has a mentor, or `"No mentor assigned"` otherwise.

3. **Challenge**: Allow a professor to mentor multiple students and keep track of them.  
   - Use a list in the `Professor` class to store the names of the students they mentor.  
   - Add a `get_mentored_students()` method to the `Professor` class to return a list of names of their mentored students.  

**Example Output**:  
```python
# Example
professor.mentor_student(student)
student.get_mentor()  # Returns: "Dr. Smith"
professor.get_mentored_students()  # Returns: ["Alice Johnson"]
```  
