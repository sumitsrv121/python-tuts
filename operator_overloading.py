class Student:
    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):
        return Student(self.marks1 + other.marks1, self.marks2 + other.marks2)

    def __str__(self):
        return f"{self.marks1} {self.marks2}"

    def __gt__(self, other):
        total_marks_for_self = self.marks1 + self.marks2
        total_marks_for_other = other.marks1 + other.marks2
        return total_marks_for_self > total_marks_for_other


s1 = Student(10, 20)
s2 = Student(15, 15)

s3 = s1 + s2

print(s3)


if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
