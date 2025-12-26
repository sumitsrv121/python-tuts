a = 5
b = 0
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Division by zero")
except Exception as e:
    print("Unknown exception:", e)

finally:
    print("finally statement")
