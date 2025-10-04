
def add(i,j):
    return i+j
def division(i,j):
    if j!=0:
        return i/j
    else:
        return "zero division error"
my_subtract = lambda i,j:i-j
my_divide = lambda i,j:i/j if j!=0 else "zero division error"

def calculate(fn,i,j):
    return fn(i,j)
print(calculate(add,1,2))
print(calculate(division,1,0))
print(calculate(my_subtract,1,2))
print(calculate(lambda i,j:i/j if j!=0 else "zero division error",1,2))


