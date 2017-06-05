#coding = utf -8

class Car:
    """一次模拟汽车的尝试"""
    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make  = make
        self.module = model
        self.year = year
    def get_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)+" "+self.make+" " +self.module
        return long_name.title()

my_newcar = Car("audi","a8","2016")
print(my_newcar.get_name())