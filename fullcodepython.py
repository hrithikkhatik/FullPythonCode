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

#filter
def even(a):
    return a%2==0
numbers = [1,2,3,4,5,6,7]
ans = filter(even,numbers)
print(ans)

def even(a):
    return a%2==0
numbers = [1,2,3,4,5,6,7]
ans = list(filter(even,numbers))
print(ans)

def even(a):
    return a%2==0
numbers = [1,2,3,4,5,6,7]
ans = set(filter(even,numbers))
print(ans)

def even(a):
    return a%2==0
numbers=[1,2,3,4,5,6,7]
ans = set(filter(lambda a:a%2==0,numbers))
print(ans)

ans = set(filter(lambda a:a%2==0,range(11)))
print(ans)

# map()
def squares(a):
    return a**2
numbers = [1,2,3,4,5]
ans = list(map(squares,numbers))
print(ans)

def squares_1(b):
    return b**2
numbers_1 = [1,2,3,4,5]
res = list(filter(squares_1,numbers_1))
print(res)

def squares(a):
    return a%2==0
numbers=[1,2,3,4,5]
ans=list(map(squares,numbers))
print(ans)

numbers=[1,2,3,4,5]
ans = list(map(lambda a:a**2,numbers))
print(ans)

ans = list(map(lambda a:a**2,range(6)))
print(ans)







