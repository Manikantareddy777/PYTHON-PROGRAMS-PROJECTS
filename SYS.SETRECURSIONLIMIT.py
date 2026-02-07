import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def greet():
    for i in range(1,2000):
        
        print(i,"hello")
        i=i+1
    
    
greet()