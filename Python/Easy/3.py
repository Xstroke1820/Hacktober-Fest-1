def greet():
    print("Hello, world!")

def add(a, b):
    return a + b

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

greet()

a = int(input("enter a number "))
b = int(input("enter a number "))   
print(add(a,b))  
