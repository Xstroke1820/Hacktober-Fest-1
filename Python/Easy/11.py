def outer():
    x = 10

def inner():
     x # Error: x is local to outer and cannot be made global
x = 5
inner()
print(x)

outer()
print(x)