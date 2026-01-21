class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def role(self):
        return "Employee"
class Manager(Employee):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.__bonus = bonus
    def role(self):
        return "Manager"
    def bonus(self):
        return self.__bonus
    def get_salary(self):
        base = super().get_salary()
        return base + self.__bonus
def show_info(staff):
    for person in staff:
        print(f"Name: {person.name}; Role: {person.role()}; Salary: {person.get_salary()}")
m = Manager("Ali", 19, 500, 1000)
e1 = Employee("Islam", 19, 300)
e2 = Employee("Alish", 18, 150)
staff = [m, e1, e2]
show_info(staff)