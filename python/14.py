
print("""

    1)Ankara
    2)İstanbul
    3)İzmir
    4)Antalya

 """)



a = input("Herhangi bir şehir belirleyiniz :")
a = int(a)

if a == 1:
	print("Ankara'yı seviyor musunuz ?")

elif a == 2:
	print("İstanbul'un neyi meşhur ?")

elif a == 3:
	print("İzmir'i neden seçtiniz ?")

elif a == 4:
	print("Antalya'nın hangi plajı daha iyidir ?")	

else :
	print("Hatalı seçim yaptınız!")
