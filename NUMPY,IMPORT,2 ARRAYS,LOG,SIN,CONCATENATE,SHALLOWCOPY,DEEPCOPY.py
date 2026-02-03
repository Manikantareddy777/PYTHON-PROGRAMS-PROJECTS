'''array add +5 number
add two array
use sin,cos,tan,cot,cosec,cosec
concatenate
log
.vew=shallow
.cpy=deep'''
from numpy import *
arr=array([1,2,3,4,5,6,7])
print(arr)

mounika=array([1,2,3,4,5,6])
arr1=mounika+5
print(arr1)

pavan=array([1,3,5,6,45,6])
arr1=(tan(pavan))
print(arr1)
print(id(arr1))
print(type(arr1))

siva=array([1,2,34,4,5,6,4,8])
swathi=array([1,2,3,4,55,5,5,5])
print(siva+swathi)

muni=array([1,4,2,3,5,4,5,8])
sumanth=array([1,2,3,4,5,5])
good=concatenate([muni,sumanth])
print(good)

mo=array([2,100,4,5,56,10])
mm=log(mo)
print(mm)

print("///shallow copy")
bharath=array([2,3,4,5,6,7,7])
bha=bharath.view()
bha[1]=7
print(bha)
print(bharath)

print("////deep copy")
jj=array([1,3,4,5,56,3,3])
jjj=jj.copy()
jj[1]=7
print(jj)
print(jjj)

arr1=array([1,2,2])
arr2=array([1,5,9])
result=[]
for i in arr1:
    result=arr1+arr2
print(result)

    
    
    



