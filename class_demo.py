class Computer:
    def __init__(self, cpu, mem):
        self.cpu = cpu
        self.mem = mem

    def config(self):
        print(self.cpu, str(self.mem) + "gb", "1TB")


computer = Computer("i5", 16)
computer.config()
