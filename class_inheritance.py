class Person:
    name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getinfo(self):
        print(f"this person's name {self.name} and they are {self.age} years old")

class Student(Person):
    nis = ""

    def __init__(self, name, age, nis, grade):
        super().__init__(name, age)
        self.nis = nis
        self.grade = grade
    def getinfo(self):
        print(f"this student's name {self.name} they are {self.age} years old and they are in grade {self.grade}")
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

Person1 = Person("Afifa", 30)
Person1.getinfo()

Student1 = Student("Afifah", 16, "275783426", "musyrifah")
Student1.study("Math")
Student1.getinfo()


