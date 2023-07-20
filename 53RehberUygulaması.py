rehber = {
    "kişi1":{
        "Cep":"1111111",
        "İş":"1111111",
        "Ev":"1111111"
    },
    "kişi2":{
        "Cep":"2222222",
        "İş":"2222222",
        "Ev":"2222222"
    }
}
isimler = rehber.keys()

kisi = input("Kişi Adı: ")
tel = input("istediğiniz Telefon : ")

if kisi in isimler:
    flag  = True
else:
    flag = False

if flag:
    print(rehber.get(kisi).get(tel,"istediğiniz Bilgi Mevcut Değil!"))
    input("Ana menüye dönmek için enter'e basın!")

else:
    print("Aradığıınız Kişi Bulunamadı!")
    input("Ana menüye dönmek için enter'e basın!")
