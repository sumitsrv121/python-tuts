class IntelliJ:
    def support_coding(self):
        print("prompt")
        print("compile")
        print("execute")


class PyCharm:
    def support_coding(self):
        print("prompt")
        print("compile")
        print("interpret")


class Laptop:
    def start_coding(self, ide):
        ide.support_coding()


intellij = IntelliJ()
pycharm = PyCharm()

laptop = Laptop()
laptop.start_coding(intellij)
laptop.start_coding(pycharm)
