'''

     datatype
     ndim
     size
     flatten
     reshape
     max
     min
     matrix
     matrix
     

'''
from numpy import *
arr1=array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.size)
print(arr1.flatten())
print(arr1.reshape(3,2))
print(arr1.min())
print(arr1.max())
m=matrix(arr1)
print(m)
print("////matrix")
mm=matrix('1 2 3 4 5 ; 6 7 8 9 0')
print(mm)
mmm=matrix('1 3; 4 5; 52 3; 45 6')
print(mmm)
print("//diagonal")
print(diagonal(mmm))
m11=matrix('1 2 3 ;4 5 6;7 8 9')
m22=matrix('1 2 3 ;4 5 6;7 8 9')
m33=m11+m22
print(m33)
m44=m11*m22
print(m44)