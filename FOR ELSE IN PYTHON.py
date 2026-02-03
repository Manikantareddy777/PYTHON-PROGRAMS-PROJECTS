'''
else in for loop

'''
print("//finding")
nums=[1,2,3,4,5,6]
for num in nums:
    if(num%5==0):
        print(num)
        
print("////break")
numbers =[1,2,25,15,10]  
for num in numbers:
    if(num%5==0):
        print(num)
        break

print("///else .....")
numbers=[1,2,3,4,5,6]
for num in numbers:
    if(num%5==0):
        print(num)
        break
    else:
        print("not found")


