def add(i,j):
    return i+j
def subtract(i,j):
    return i-j
def multiply(i,j):
    return i*j
def divide(i,j):
    if j!=0:
        return i/j
    else:
        return "zero division error"
a=add
print(a(1,2))
def pas(i,j):
    return subtract(i,j)
print(pas(1,2))
def calculator(i,j,func):
    return func(i,j)
print(calculator(1,2,multiply))
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,0))