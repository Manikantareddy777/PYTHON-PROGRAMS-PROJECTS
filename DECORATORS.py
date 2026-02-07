def decorator(func):
    def muni():
        print("muni ")
        func()
        print("mani")
    return muni
@decorator
def say():
    print("hello")
say()

print("/////another one")
def m():
    def ka():
        print("hi")
    ka()
    print("s")
m()