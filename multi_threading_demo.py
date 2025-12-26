from threading import Thread
from time import sleep


class Hello:
    def greeting(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi:
    def greeting(self):
        for i in range(5):
            print("hi")
            sleep(1)


t = Thread(target=Hi().greeting)
t1 = Thread(target=Hello().greeting)
t1.start()
sleep(0.2)
t.start()


t.join()
t1.join()

print("bye")
