def hipo(a,b,c):
	if a**2 + b**2 == c**2:
		return "Bu üçgenin bir açısı 90 derecedir!"
	else:
		return "Bu üçgenin bir açısı 90 derece değildir!"


print(hipo(3,4,5))
print(hipo(3,7,9))

# return ile ifade belirtebiliriz.