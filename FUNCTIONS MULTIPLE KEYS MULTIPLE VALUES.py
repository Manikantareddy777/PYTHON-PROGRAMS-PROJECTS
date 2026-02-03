'''
keywords variable length arguments in python
'''
def person(name,*data):
    print(name)
    print(data)
person('muni',28,'mumbai',960344)

print("//////mutliple keys and multiple values")
def person2(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        
        print(i,j)
person2('jyothi',age='24',location='yeturu',mobile=95021)

