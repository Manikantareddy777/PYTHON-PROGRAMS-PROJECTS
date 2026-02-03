'''

global vs local value
using global keyword we get same values in inner and outer

'''
a=10
def something(): 
    global a
    a=15
    print(a)
something()
print(a)

print("/////without global")
a=10
def something(): 
    a=15
    print(a)
something()
print(a)

print("///globals of a")
a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print("in fun",a)
globals() ['a']=20
something()
print(a)



