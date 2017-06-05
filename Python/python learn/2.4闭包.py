#coding:utf-8
def addx(x):
    def addr(y):
        return x + y
    return addr
c = addx(8)
print (c.__name__)
print (c(10))


def fun1(num):
    """在函数中连续定义一个函数"""
    print("fun1:",num)
    def fun2(num1):
        print("fun2",num1)
        return num1 + num
    return fun2

res = fun1(20)
print(res)
print(res(30))

def foo():
    """闭包经典例子"""
    m = 0
    def fool():
        m = 1
        print(m)#====>②
    print(m)#====>①
    fool()
    print(m)#===>③
foo()


#当调用函数时，函数会把自己的闭包函数体导入，来分析它的局部变量，python规定左边的为局部变量，
def foo():
    a = 1
    def bar():
        b = a + 1
        return b
    return bar
c = foo()
print (c())


def foo():
    a = [1]
    def bar():
        a[0] = a[0] + 1
        return a[0]
    return bar
c = foo()
print (c())

