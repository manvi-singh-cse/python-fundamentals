class Employee:                                                            # parent class

    company_name = "Google"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_employee_detail(self):
        print(f"Hey! My name is {self.name}. I am an employee at {self.company_name} with employee id {self.employee_id}.")

class Coder:                                                               # multiple inheritance

    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def get_coder_detail(self):
        print(f"Hey! I am {self.name}, a coder in {self.language} language.") 

class Programmer(Employee, Coder):                                         # multiple inheritance

    def __init__(self, name, employee_id, language):
        Employee.__init__(self, name, employee_id)
        Coder.__init__(self, name, language)

    def get_programmer_detail(self):
        print(f"Hey! I am a programmer at {self.company_name} in {self.language} language.")

class Manager(Programmer):                                                 # multi-level inheritance

    def __init__(self, name, employee_id, language, department):
        super().__init__(name, employee_id, language)                      # super() to call parent constructor
        self.department = department
    
    def get_manager_detail(self):
        print(f"Hey! I am {self.name} , manager in {self.department} department.") 


a = Employee("Manvi", 20)
b = Coder("Bhavesh", "python")
c = Manager("Shloka", 14, "java", "IT")

print(a.employee_id)
a.get_employee_detail()

print(b.language)
b.get_coder_detail()

print(c.department)
c.get_manager_detail()