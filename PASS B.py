'''

count by ///pass by value//

'''

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
lst=[1,2,3,4,5,6,7,8,9,10]
even,odd=count(lst)
print("even:",even)
print("odd:",odd)