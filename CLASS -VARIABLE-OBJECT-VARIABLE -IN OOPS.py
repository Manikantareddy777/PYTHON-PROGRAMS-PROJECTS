class car:
    wheels=4
    def __init__(self):
        self.mil=8
        self.company="BMW"

c1=car()
c2=car()
c2.mil=10
c2.company="tech mahendra"
c2.wheels=11

print(c1.company,c1.mil,c1.wheels)
print(c2.company,c2.mil,c2.wheels)

class student:
    school=4
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        return (" student is good ")
s1=student(1,2,3)
print(s1.avg())
print(s1.info())


class student:
    school=4
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
