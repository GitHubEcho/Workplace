#coding = utf-8
def city_country(city,country):
	"""函数输出城市 国家的键值对"""
	name = ("\'"+city+","+country+"\'")
	return name.title()

a = city_country('shanghai','China')
print a 
b = city_country('bali','france')
print b
