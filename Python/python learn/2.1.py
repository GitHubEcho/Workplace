#coding utf- 8
"""class using"""
class Ball:
    def setname(self,name):
        self.name = name
    def clik(self):
        print ("我是球%s，谁在替我。。"%self.name)

a = Ball()
a.setname("球A")

b = Ball()
b.setname("球B")

c = Ball()
c.setname("int")

a.clik()
b.clik()
c.clik()
