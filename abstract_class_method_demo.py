from abc import ABC

from black.trans import abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("processing & running tasks")


class Programmer:
    @staticmethod
    def solve(com: Computer):
        print("solve bug")
        if isinstance(com, Computer):
            com.process()


c = Laptop()
p = Programmer()
p.solve(c)
