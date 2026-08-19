class Employee:
    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dep) 
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 70000) 

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().showDetails()

emp = Employee("Freelancer", "Finance", 60000)
print("--EMPLOYEEE--")
emp.showDetails()
eng = Engineer("Ali", 30)
print("--ENGINEER--")
eng.show()
