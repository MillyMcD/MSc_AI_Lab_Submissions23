class Student:    
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.modules_list = []
    
    def print_student_info(self):
        print("Student name: %s" %self.name)
        print("Student ID: %s" %self.student_number)
        print("module/s undertaken by the studen:" )
        i = 0
        for c in self.modules_list:
                i+=1
                print("%d %s" %(i,c.print_module_info()))
        
    def enrol(self, module_running):
        self.modules_list.append(module_running)



class Module:  
    def __init__(self, module_title, module_credits, department):
        self.module_title = module_title
        self.credits = module_credits
        self.department = department
    
    def print_module_info(self):
        return "%s, Credits: %s, Department: %s" %(self.module_title, self.credits, self.department)
    
def main():
    student_one=Student("Holly Time",1234567)
    student_two=Student("Irvine Worm",1234568)

    mod_one=Module("Art",100,"ADM")
    mod_two=Module("Fashion",120,"ADM")
    mod_three=Module("AI",100,"CEBE")

    student_one.enrol(mod_one)
    student_one.enrol(mod_two)

    student_two.enrol(mod_two)
    student_two.enrol(mod_three)

    student_one.print_student_info()
    print("")
    student_two.print_student_info()

main()

#Besher this is soemthing I need to work on, as it was very difficult to complete these tasks!
