import os
# os kütüphanesini terminalini dahil etmek
kitapListe = list()

menü = """
              KÜTÜPHANEYE HOŞGELDİNİZ
1)Kitap Ver
2)Kitap Al
3)Tümünü Listele
Q)Çıkış

"""
# tuple tanımlama grubu anlamına gelir
def kitapVer(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Verdiğiniz kitap için teşekkür ederiz...")
    input("Ana menüye dönmek için enter'e basın!")

def kontrol(kitap:tuple,liste:list):
    if liste in liste:
        return True
    else:
        return False
def kitapAl(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitabı başarıyla aldınız, iyi okumalar...")
        input("Ana menüye dönmek için enter'e basın!")
    else:
        print("İstediğiniz kitap mevcut değildir!")
        input("Ana menüye dönmek için enter'e basın!")
def listele(liste:list):
    for a in liste:
        print("Kitap Adı: {}      Yazar : {} ".format(a[0],a[1]))
    input("Ana menüye dönmek için enter'e basın!")

while True:
    os.system("cls")
    # clear anlamında ')
    print(menü)

    secim = input("İşlem Numarasını Giriniz : ")

    if secim =="1" :
        kitap_ismi = input("Kitabın Adı : ")
        yazar = input("Yazar : ")
        kitap = (kitap_ismi,yazar)
        kitapVer(kitap,kitapListe)
    elif secim =="2" :
        kitap_ismi = input("Kitabın Adı : ")
        yazar = input("Yazar : ")
        kitap = (kitap_ismi, yazar)
        kitapAl(kitap,kitapListe)
    elif secim =="3" :
        listele((kitapListe))
    elif secim == "q" or secim =="Q" :
        print("Görüşmek Dileğiyle Keyifli Okumalar....")
        quit()
    else:
        print("Hatalı Giriş Yaptınız!")
        input("Ana menüye dönmek için enter'e basın!")
