def person(name, **kwargs):
    print(name)
    print(kwargs)

person('John', age=20, hobbies=['programming', 'python'])