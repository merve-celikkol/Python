liste = ["Ankara","İstanbul","Adana","Konya"]

liste2 = liste.copy()

print(liste)
print(liste2)
print(50*"=")

liste.append("Muğla")
liste.remove("Ankara")
liste2.append("Çanakkale")
liste2.extend(liste)
# liste2 içerisine liste yi ekler. Aynı olması önemsiz

print(liste)
print(liste2)
print(50*"=")
print(liste2.count("Ankara"))
# Kaç adet olduğunu yazdırır.
print(50*"=")
liste2.sort()
print(liste2)
# sort alfabetik ve saısal sıralama yapar.
print(50*"=")
liste3 = [1,2,3,7,8,56,43,3,456,5,4,23,6]
print(liste3)
liste3.sort()
print(liste3)