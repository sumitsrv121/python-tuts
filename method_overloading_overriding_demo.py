class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def add(self, a=None, b=None, c=None):
        s = 0
        if a is not None:
            s += a
        if b is not None:
            s += b
        if c is not None:
            s += c
        return s


s1 = Student(5, 9)
print(s1.add(5, 6))
print(s1.add(5, 6, 7))
print(s1.add(5))


class A:
    def show(self):
        print("show of A")


class B(A):
    def show(self):
        print("show of B")


b = B()
b.show()
