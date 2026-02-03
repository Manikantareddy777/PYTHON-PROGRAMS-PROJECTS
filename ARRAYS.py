from array import *

arr=array('i',[1,2,3,4,5])
print(arr)

arr=array('I',[1,2,3,4,5])
print(arr)

print(arr.buffer_info())

mani=array('i',[1,2,3,4,5,6])
print(mani[0])
for i in mani:
    print(i)
for i in range(6):
    print(mani[i])
    
mani.reverse()
print(mani)

newarr=array(mani.typecode,(a*a for a in mani))
for i in newarr:
    print(i)
