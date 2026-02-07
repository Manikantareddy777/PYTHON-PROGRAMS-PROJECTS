'''
MULTIPLE inheritance
A()
B()
C()
D(A,B,C)

MULTIPLE level inheritance
A()
B(A)
C(B)
D(C)'''

print("////////multiple inheritance")
class A:
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")
class B:
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")
class C(A,B):
    def feature5(self):
        print("feature5 working")

a=A()
a.feature2()
print("/////")
c1=C()
c1.feature5()
c1.feature4()
c1.feature3()
c1.feature2()
c1.feature1()


print("//////////multi level inheritance")
class A:
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")
class B(A):
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")
class C(B):
    def feature5(self):
        print("feature5 working")
print("/////////////")
c11=C()
b11=B()
b11.feature1()
c11.feature2()
c11.feature3()
c11.feature4()
c11.feature5()

print("//////////////////////__init__MULTIPLE level inheritance")
class A:
    def __init__(self):
        print("__init__ A  in   MULTIPLE level inheritance")
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")
class B(A):
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")
class C(B):
    def feature5(self):
        print("feature5 working")
c111=C()

print("/////////MULTIPLE inheritance")
class A:
    def __init__(self):
        print("__init__ A  in   MULTIPLE inheritance")
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")
class B():
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")
class C(A,B):
    def __init__(self):
        print("__init__ c  in   MULTIPLE inheritance")
    def feature5(self):
        print("feature5 working")
c1111=C()