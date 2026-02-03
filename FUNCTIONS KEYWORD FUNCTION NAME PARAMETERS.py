'''
function 
>>To perform a specific task
'''
def greet():
    print("hello world")
    print("hi mani")
greet()

print("//////////")
def add(x,y):
    c=x+y
    return c
greet()
result=add(5,4)
print(result)

print("//////////")
def sub_add(x,y):
    c=x+y
    d=x-y
    return c,d
result1=sub_add(5,5)
print(result1)
result2=sub_add(11,22)
print(result2)
x=int(input("enter a number:"))
y=int(input("enter a number:"))
result3=sub_add(x,y)
print(result3)




