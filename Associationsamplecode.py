class Instructor:
    def __init__(self, name):
        self.name = name
        self.courses = []  

class Course:
    def __init__(self, course_code, instructor):
        self.course_code = course_code
        self.instructor = instructor
        instructor.courses.append(self)  

