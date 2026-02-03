number=int(input("Enter a number:"))
count=0
i=1
while(number%i==0):
    count=count+1
    i=i+1
if(count==2):
    print("Not Prime number")
else:
    print(" Prime number")
    

    