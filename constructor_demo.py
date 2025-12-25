class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def computer_config(self):
        print("name:", self.name, "age:", self.age)

    def compare(self, other):
        return self.age == other.age and self.name == other.name
