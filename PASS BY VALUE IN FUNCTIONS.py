'''
function arguments in pyton
'''
x=1000
def update(x):
    x=10
    print(x)
    print(id(x))
update(x)

print("//////newwwww")
lst=[10,20,30]
print(id(lst))
print("//////")
def update(lst):
    lst[1]=25
    print(lst)
    print(id(lst))
update(lst)
