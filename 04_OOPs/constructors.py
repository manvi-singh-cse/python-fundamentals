# default or parametrized constructor, is called automatically when an instance is created. 

class Student:
    college = "DIT University"

    def __init__(self, name, rollNo):            # constructor 
        self.name = name
        self.rollNo = rollNo

    def get_info(self):
        print(f"Student name is {self.name} and roll no is {self.rollNo}. College name is {self.college}")

student1 = Student("Manvi", 20)
student1.get_info()