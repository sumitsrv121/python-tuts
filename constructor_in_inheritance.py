class A:
    def __init__(self):
        print("Class A")

    def feature1(self):
        print("feature1 is working in class A")

    def feature2(self):
        print("feature2 is working")


class B:
    def __init__(self):
        print("Class B")

    def feature1(self):
        print("feature1 is working in class B")

    def feature4(self):
        print("feature4 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("Class C")


c = C()
c.feature1()
