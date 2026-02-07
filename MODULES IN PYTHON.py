print(__name__)


a=9
b=1
def add(a,b):
    print(a+b)
add(a,b)

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b

a=9
b=2
c=add(a,b)
print(c)
d=sub(a,b)
print(d)