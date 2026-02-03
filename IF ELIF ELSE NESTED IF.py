'''

if elif else statements

'''
print('''/////boolean statements//// ''')

if True:
    print("i am right")
    
print('''///// if statements//// ''')

x=8
r=x%2
if(r==0):
    print("even")
    
    
print('''/////if else statements//// ''')

x=7
r=x%2
if(r==0):
    print("even")
else:
    print("odd")

print('''///if elif///''')
y=6666
z=y%2
if(z==0):
    print("even")
elif(z!=0):
    print("odd")
print("bye")

print('''/////nested if statements//// ''')
a=9
b=a%2
if(b==0):
    print("divisible by 2")
    if(a>5):
        print("greater")
    else:
        print("not so great")
else:
    print("odd")