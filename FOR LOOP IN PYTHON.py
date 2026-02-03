'''
in for loop

'''
x=['navin',2,23]
print(x)
for i in x:
    print(i,end="\n")
    
    
y='navin'
for i in y:
    print(i)
    
print("//////for loop///////")

for i in range(100):
    print("hi",i)

print("//////for in range ///////")
for i in range(2,101,2):
    print(i)
print("//////for in range////////")
for i in range(0,101,5):
    print(i,end=" ")
print("///// eliminates 5 multiples/////")
for i in range(10,25,1):
    if(i%5!=0):
        print(i)
print("/////i want five table////")
for i in range(1,11):
    print("5 x ",i,"=",i*5 )

print("/////printing perfect square numbers from 1 to 500")
for i in range(1,501):
    if(i**0.5==int(i**0.5)):
        print("perfect square number",i)

print("///for even numbers////")
for i in range(2,1000,2):
    print(i,end=" ")
    
print("///wending machine")
i=1
x=int(input("how many candies you want:"))
while(i<=x):
    print(i,end=" candy\n")
    i=i+1
print("bye,,,i given your amount of candies")

print("///break condition using for out of stack")

av=15
x=int(input("enter candies:"))
i=1
while(i<=x):
    if(x>av):
        print("out of stack\n  available candies are 15")
        break
    else:
        print(i,end=".candy \n")
    i=i+1
    
print("////continue statement condition")
for i in range(1,100):
    if(i%3==0):
        continue
    print(i,end=" ")

print("/////skipping 3 and 5 multiples from 1 t0 100 using gates")
for i in range(1,100):
    if(i%3==0 or i%5==0):
        continue
    print(i)
    
print("///using pass don't print even numbers")  
for i in range(1,10):
    if(i%2==0):
        pass
    else:
        print(i)


    

    



    