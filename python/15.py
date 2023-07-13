a = input("İlk Sayıyı Giriniz      : ")
a = float(a)
c = input("Yapılacak İşlem         : ")
b = input("ikinci Sayıyı Giriniz   : ")
b = float(b)

if c == "+":
	print("Sonuç                   :",a+b)
elif c == "-":
	print("Sonuç                   :",a-b)
elif c == "/":
	print("Sonuç                   :",a/b)
elif c == "*":
	print("Sonuç                   :",a*b)
elif c == "**":
	print("Sonuç                   :",a**b) 
	# üssünü almak
else:
	print("Hatalı ifade kullandınız! ")