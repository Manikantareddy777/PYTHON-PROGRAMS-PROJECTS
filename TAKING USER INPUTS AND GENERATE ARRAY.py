from array import *
mani=array('i',[])
n=int(input("enter the length of array:"))
for i in range(n):
    x=int(input("enter a value:"))
    mani.append(x)
print(mani)
val=int(input("search a number:"))
k=0
for e in mani:
    if(e==val):
        print(val)
        print(mani.index(val))
mani.reverse()
print(mani)
mani.remove(9)
print(mani)
