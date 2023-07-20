sözlük = {"Siyah":"Kara","Ak":"Beyaz", "Abide":"Anıt","Adet":"Tane"}

giris = input("Kelime Giriniz : ")

print(sözlük.get(giris,"Aradığınız kelime bulunamadı!"))

# yanlış input alınması durumunda programın çökmemesi sağlandı.