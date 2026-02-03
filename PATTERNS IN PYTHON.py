print("#",end="")
print("#")


for j in range(4):
    print("#",end=" ")
print("///one")
for j in range(4):
    print("#",end=" ")
    
print("///two\n")

for j in range(5):
    for i in range(5):
        print("#",end=" ")
    print()

print("////three")
for i in range(4):
    print(i)
    for j in range(i):
        print("#")
    print()
    

for i in range(6):
    for j in range(1+i):
        if(j==0):
            continue
        print(j,end=" ")
    print()
    
print("////four")
for i in range(10):
    for j in range(10-i):
        print("*",end=" ")
    print()
    
for i in range(7):
    for j in range(i+1):
        print("&",end=" ")
    print()
for i  in range(7):
    for j in range(6-i):
        print("*",end=" ")
    print()
    
for i in range(7):
    for j in range(1+i):
        print("*",end=" ")
    print()
for j in range(7):
    for i in range(6-j):
        print("*",end=" ")
    print()
    
    
rows = 5

# Top half including middle
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()

# Bottom half
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()


print("////pyramid")
rows=5
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*i+1))
    
    

    
    


    