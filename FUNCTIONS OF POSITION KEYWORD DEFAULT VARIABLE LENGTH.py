'''
types of arguments

position
keyword
default
variable length
>>>*b multiple values
'''
def add(a,b):
    c=a+b
    print(c)
add(5,6)




print("///////position")
def person(name,age):
    print(name)
    print(age)
person('vijaya',15)




print("/////keyword")
def phone(companyname,gb,storage):
    print(companyname)
    print(gb)
    print(storage)
phone(storage=128,companyname='poco',gb=6)




print("/////default")
def dad(name,age=45,weight=60):
    print(name)
    print(age)
    print(weight)
dad('bhadra reddy')



print("//////variable length arguments")
def sum(a,*b):
    print(a)
    print(*b)
sum(2,3,4,4,5,6,6,7)


print("///summation")
def summation(a,*b):
    x=a
    for i in b:
        x=x+i
    print(x)
summation(1,2,3,4,5,5,6,7)


print("/////mani")
def mani(*b):
    n=0
    for i in b:
        n=n+i
    print(n)
mani(5,5,5,5,5,5,5,5,5)



