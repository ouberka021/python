class Person:
    def __init__(self, name: str = "Unknown", age: int = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

