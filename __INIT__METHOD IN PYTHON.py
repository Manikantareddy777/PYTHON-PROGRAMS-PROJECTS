class computer:
    def __init__(self):
        self.name='nam'
        self.age=20
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c1.age=20
c2=computer()
if c1.compare(c2):
    print(" same ")
else:
    print(" different ")

    

























