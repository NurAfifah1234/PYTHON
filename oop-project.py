class Student:
    name = ""
    grade = ""

    def __init__(self, Student_name, Student_grade):
        self.name = Student_name
        self.grade = Student_grade
    def makesubject(self, subject):
        print(f"{self.name} kelas {self.grade} belajar {subject}")
        

santriw = Student("Afifah", "Musyrifah")  

print(type(santriw))

santriw.makesubject("Biologi")