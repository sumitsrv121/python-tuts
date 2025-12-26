from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(0.5)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.25)
t2.start()
