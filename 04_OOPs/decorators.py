class Employee:
    employee_id = 31

    def show_my_id(self):
        print(f"The employee id in instance is {self.employee_id}")
    
    @classmethod                                                  # classmethod decorator to access class directly through instance
    def show(cls):
        print(f"The employee id in class is {cls.employee_id} right now")

    @classmethod
    def change_id(cls, new_id):
        cls.employee_id = new_id

    @property                                                     # property decorator to access a method like an attribute.
    def name(self):
        return (f"{self.fname} {self.lname}")
    
    @name.setter                                                  # settter to set value of 'name' property 
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    @staticmethod                                                 # works without self/cls parameter
    def greet():
        print("Hey there")

manvi = Employee()

manvi.employee_id = 20
print("Instance attribute set to 20 ")

manvi.show()

manvi.change_id(manvi.employee_id)                                # change class attribute using @classmethod decorator
print("Class attribute changed to 20 ")
manvi.show()

manvi.greet()
manvi.name = "Manvi Singh"                                        # set name using name.setter decorator
print(manvi.name)                                                 # same as print(manvi.fname, manvi.lname)