def fact(n):
    if n==0:
        return 1
    
        
    return n*fact(n-1)
result=fact(5)
print(result)

f=lambda a:a*a
result=f(5)
print(result)

f=lambda a,b:a+b
result=f(5,2)
print(result)

def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8]
evens=list(filter(is_even,nums))
print(evens)

def is_odd(n):
    return n%2!=0
nums=[1,2,3,4,5,6,7,8]
odds=list(filter(is_odd,nums))
print(odds)

def is_odd(n):
    return n%2!=0
nums=[1,2,3,4,5,6,7,8]
odds=list(filter(is_odd,nums))
print(odds)



    