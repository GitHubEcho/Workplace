#coding = utf-8
class Ball:
    def __init__(self,name):
        self.name = name
    def click(self):
        print("我是%s,谁在踢我"%self.name)

b = Ball("int")
b.click()