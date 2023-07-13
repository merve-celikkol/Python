kitapListe = list()

menü = """

1)Kitap Ekle
2)Kitap Çıkar
3)Kitapları Göster
Q) Çıkış

"""

def kitapEkle(liste,kitap):
    liste += [kitap]
    print("Kitap Eklendi!")
    input("Ana menüye dönmek için enter'e basınız!")

def kitapÇıkar():
    pass
def listele(liste):
    for a in liste:
        print("Kitap Adı >>>>>>> ",a)
    ### print("kitap Adı >>>>>>> {}".format(a) üstteki kod bu şekilde de olabilir ')
    input("Ana menüye dönmek için enter'e basınız!")
def çıkış():
    quit()

while True:
    print(menü)

    seçim = input("Seçiminiz : ")

    if seçim == "1":
        kitapAdı = input("Kitap Adı: ")
        kitapEkle(kitapListe,kitapAdı)
    elif seçim == "2":
        kitapÇıkar()
    elif seçim == "3":
        listele(kitapListe)
    elif seçim == "Q" or seçim == "q":
        çıkış()
    else:
        print("Hatalı Girdiniz!")
        input("Ana menüye dönmek için enter'e basınız!")