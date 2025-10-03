#functional programming
def add(i,j):
    return i+j
res = add(1,2)
print(res)
def add(i,j):
    return i+j
a=add
res = a(1,2)
print(res)
def add(i,j):
    return i+j
def call(i,j):
    return add(i,j)
res = call(1,2)
print(res)
def add(i,j):
    return i+j
def call(i,j):
    return add(i,j)
def pas(i,j,fn):
    return fn(i,j)
res=pas(1,2,call)
print(res)
# lambda function
def add(a):
    return a+1
res =add(1)
print(res)

fun = lambda a:a+1
res = fun(2)
print(res)

def add(a,b):
    return a+b
res = add(1,2)
print(res)

fun = lambda a,b:a+b
res = fun(2,5)
print(res)


