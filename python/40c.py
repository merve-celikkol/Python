listeler = ["Ankara","İstanbul","Adana","Konya"]

for a in listeler:
    print(a)
giris = input("Şehir Ekleyin : ")

listeler += [giris]
for b in listeler:
    print(b)
