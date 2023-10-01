class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_profile_info(self):
        return "Name: %s, Phone number: %s" %(self.name, self.phone_number)


class Student(Person):

    def __init__(self, course, *args, **kwargs):
        self.course = course
        self.classes = []
        super().__init__(*args, **kwargs)

    def enrol(self, module):
        self.classes.append(module)


class StaffMember(Person):

    def __init__(self, *args, **kwargs ):
        self.courses = []
        super().__init__(*args, **kwargs)

    def administrator_for(self, module):
        self.courses.append(course)

    def get_salary(self):
        return self.salary

