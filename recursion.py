import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def greet():
    print('Hello World')
    greet()

greet()