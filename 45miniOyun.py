Savaşçı = {"Güç": 165,
           "Sp" : 70,
           "STR": 175,
           "HP" : 4050}
Sura = {"Güç" : 130,
        "Sp"  : 160,
        "STR" : 40,
        "HP"  : 2560}
def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Güç"]
    vurulan["HP"] = vurulan["HP"] - eksilen

input("Vurmak için enter'e basınız!")
vur(Savaşçı,Sura)
print("Sura'nın canı :", Sura["HP"])

input("Vurmak için enter'e basınız!")
vur(Sura,Savaşçı)
print("Savaşçı'nın canı :",Savaşçı["HP"])


