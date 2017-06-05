# coding = utf-8
def music(singer, music):
    """输出歌手和专辑的函数"""
    name = singer + ":" + music

    return name.title()


a = music('heqian', 'hello')
print(a)

while True:
    print("please input :")
    s = input("input your singer:")
    if s == 'q':
        break

    m = input("input your music:")
    if m == 'q':
        break

    b = music(s,m)
    print(b)
