# Molnár Krisztina Führinger Zsófia 10.c - Első Beadandó 
import random

adatok=[]
vege=1


while vege:
    print("Válassz menüpontot!")
    print()
    print("tömb feltöltése billentyűzetről = 1\ntömb feltöltése véletlen számokkal = 2\ntömbhöz egy új elem hozzáadása = 3\na tömb egy adott sorszámú elem módosítása = 4\na tömb egy adott sorszámú elem törlése = 5\ntömb ürítése = 6\ntömb kiírása = 7\nFeladatok = 8\nkilépés = 0")

    valasz=int(input())
   
    # tömb feltöltése billentyűzetről
if (valasz==1):
        feltoltes_szama=int(input("Add meg hány számmal szeretnéd feltölteni: "))
        
        for i in range(feltoltes_szama):
            feltoltott_szamok=float(input())
            adatok.append(feltoltott_szamok)
            
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # tömb feltöltése véletlen számokkal   
    # tömbhöz egy új elem hozzáadása
    # a tömb egy adott sorszámú elem módosítása 
    # a tömb egy adott sorszámú elem törlése
    # tömb ürítése
    # tömb kiírása 
    #Feadatok
            # 1a feladat 
            # 1b feladat 
            # 1c feladat 
            # 1d feladat
    # kilépés