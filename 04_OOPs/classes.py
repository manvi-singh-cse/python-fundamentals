class Employee:                                                                       # Class 
    name = "Manvi"                                                                    # class attribute
    language = "Pyhton"
    def getinfo(self):                                                                # method
        print(f"Employee name is {self.name} and language is {self.language}")

E1 = Employee()                                                                       # Instance 
print("Employee name is ",E1.name)
print("Employee language is ",E1.language)

E1.language = "Java"                                                                  # instance attribute (preference over class attribute)
print("Employee new language is ",E1.language)

# self parameter is mandatory to be given because the E1.getinfo() gets converted into Employee.getInfo(E1).
# 1 argument is automatically given, so it must be read too.

E1.getinfo()