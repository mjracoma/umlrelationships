class Instructor:
    def __init__(self, name):
        self.name = name
        self.courses = []  
    def display_courses(self):
        return f"Instructor: {self.name}, Courses: {self.courses}"

class Course:
    def __init__(self, course_code, instructor):
        instructor.courses.append(course_code)  

inst = Instructor("Dr. Cruz")
Course("CS101", inst)
print(inst.display_courses()) 

inst2 = Instructor("Dr. Smith")
Course("CS102", inst2)
print(inst2.display_courses())