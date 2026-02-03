print("////fibonacci series///")
x=int(input("enter fibonacci number:"))
num1=0
num2=1
count=0
print(num1)
print(num2)
while(count<x):
    result=num1+num2;
    print(result)
    count=count+1
    num1=num2
    num2=result
    
    