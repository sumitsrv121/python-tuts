class Student:
    school = "Telusko"

    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

    def get_marks1(self):
        return self.marks1

    def get_marks2(self):
        return self.marks2

    def get_marks3(self):
        return self.marks3

    def set_marks1(self, marks1):
        self.marks1 = marks1

    def set_marks2(self, marks2):
        self.marks2 = marks2

    def set_marks3(self, marks3):
        self.marks3 = marks3

    @classmethod
    def get_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print(f"This is a student class in {__name__} module")


student1 = Student(34, 47, 32)
student2 = Student(89, 32, 12)


print(student1.average())
print(student2.average())


print(Student.get_school_name())

Student.info()
