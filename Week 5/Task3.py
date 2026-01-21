class Person:
    def __init__(self, name, age, fear):
        self.name = name
        self.age = age
        self.__fear = fear
    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    def greeting(self):
        print(f"Welcome, {self.name}!")
class Student(Person):
    def greeting(self):
        print(f"Welcome to the university, {self.name}!")
    def grade_sum(self, x=0, y=0, extra=0):
        total = x + y
        if extra != 0:
            total += extra
        return total
person1 = Student("Aliali", 12, "Islams")
person2 = Person("Meir", 11, "Books")
person1.show_info()
person1.greeting()
person2.greeting()
print(person1.grade_sum(4, 3))
print(person1.grade_sum(3, 4, 1))
print(person2._Person__fear)