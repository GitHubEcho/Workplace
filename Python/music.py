#coding = utf-8
def music(singer,music):
	"""miao shu yinyuezhuanji de dirct"""
	name = singer +":"+ music

	return name.title()
a = music('heqian','hello')
print (a)
 
while True:
	print ("please input :")
	s = input("input your singer:")
	m = input("input your music:")
	b = music(s,m)
