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
    def __init__(self, salary, *args, **kwargs ):
        self.courses = []
        self.salary  = salary #salary was missing?
        super().__init__(*args, **kwargs)

    def administrator_for(self, module):
        self.courses.append(module) #fixed this, should be `module`

    def get_salary(self): #now this is defined 
        return self.salary
    
# add a lecturer as a staff member with academic title
class Lecturer(StaffMember):
    def __init__(self,academic_title, *args, **kwargs ):
        self.academic_title = academic_title
        super().__init__(*args, **kwargs)
    
    def get_profile_info(self):
        #can have courses so add that
        print(f'{self.academic_title} {self.name}, Phone Number: {self.phone_number}, Salary: {self.salary}')
        for i in self.courses:
            i.print_module_info()

def main():
    #define two lecturers
    lec_one = Lecturer(academic_title='Dr',name='Dave Pillow',phone_number='07231231312',salary=45000)
    lec_two = Lecturer(academic_title='Prof',name='Alice Berger',phone_number='0723122321',salary=70000)

    lec_one.get_profile_info()
    lec_two.get_profile_info()
    

main()



