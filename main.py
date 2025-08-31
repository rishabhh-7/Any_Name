import os   # unused import
import math

x = 5
Y = 10   # bad naming style

def addNumbers(a,b): # bad function name
  return a+b   # wrong indentation (2 spaces)

def Subtract(a, b):  # bad function name
    result = a - b
    return result

def multiply(a, b):
    temp = a * b
    unused = 100   # unused variable
    return temp

def divide(a, b):
    try:
        return a / b
    except:
        print("Something went wrong")  # bare except
        return None

def circle_area(r):
    return 3.14 * r * r   # magic number

class myclass:   # bad class name
    def __init__(self, v):
        self.Value = v  # bad attribute naming

    def print_value(self):
        print("Value is:", self.Value)

def main():
    a = 10
    b = 0
    print(addNumbers(a, b))
    print(Subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))
    obj = myclass(42)
    obj.print_value()

if __name__ == "__main__":
    main()
