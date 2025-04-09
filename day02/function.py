"""
def function_name():
    Statements
    """
import numbers


def return_value():
    return  100

print(return_value())

print("-----------------------------")

def return_int() -> int:
    print("return string value")

print(return_int())

print("--------------------")
def cube(num) -> int:
    return  num * num * num
print(cube(10))

def cube(num: int ) -> int:
    return  num * num * num
#print(cube("A"))# expected type is integer

def addition(num1: numbers, num2: numbers, num3:numbers = 0) -> numbers:
    return num1 + num2 + num3

print(addition(2,2.0))
print(addition(2,20, 1.60))

print("--------------------")

def function() -> int:
    pass
