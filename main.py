class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(";")
        #adatmezők kialakitása 
        self.ssz = reszletek[0]
        self.datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.eredmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = reszletek[5]
        self.varosAllam = reszletek[6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.datum}, {self.helyszin}: {self.gyoztes} - {self.vesztes} ({self.eredmeny})"
    
    def pontKulonbseg(self):
        reszletek = self.eredmeny.split('-')
        return int(reszletek[0]) * int(reszletek[1])
    

    #0 
print("Super Bowl döntöinek feldolgozása")

#1
finp = open("SuperBowl.txt", mode="rt", encoding="UTF8")
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i  in range(1, len(adatsorok)):
    if adatsorok[i] !="":
        donto = Donto(adatsorok[1])
        dontok.append(donto)



for item in dontok:
    print(item)
print("----------------------------------------------------")

#programoozási tételek
#összegzés tétele
#Határozza meg hogy a superBowl döntöket, hány ember láttogata meg 


sum = 0
for item in dontok:
    sum += item.nezoszam
print(f"sum = {sum}")
print("----------------------------------------------------")
#átlag 
#határozza meg a látogatok számát
sum = 0
for item in dontok:
    sum += item.nezoszam
    atlag = sum / len(dontok)
print(f"átlag = {atlag:.2f}")
print("----------------------------------------------------")

#min - max tétel
#min
#Határozza meg, hogy a dömtök között milyen volt a legkisebb pont külömbség

minPontKulombseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() < minPontKulombseg.pontKulonbseg():
        minPontKulombseg = item
print(f"min pontkülömbség: {minPontKulombseg.pontKulonbseg()}")
print("----------------------------------------------------")

#max
#Határozza meg, hogy a dömtök között milyen volt a legnagyobb pont külömbség

maxPontKulombseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() > maxPontKulombseg.pontKulonbseg():
        maxPontKulombseg = item
print(f"max pontkülömbség: {maxPontKulombseg.pontKulonbseg()}")
print("----------------------------------------------------")

#határozza meg hogy a döntökön milyen volt a maximális látogatság 
maxNezoszam = dontok[0]
for item in dontok:
    if item.nezoszam > maxNezoszam.nezoszam:
        maxNezoszam = item
print(f"max nezoszam: {maxNezoszam.nezoszam}")
print("----------------------------------------------------")

#megszámlálás
#határozza meg a döntök során hányszor nyert Pittsburgh Steelers
dbPS = 0 
for item in dontok:
    if item.gyoztes == "Pittsburgh Steelers":
        dbPS += 1
print(f"A 'Pittsburgh Steelers' csapat {dbPS} gyözött a  döntök során") 
print("----------------------------------------------------")

#eldöntés tétele
#legalabb egy eleme teljesíti a feltételt
#határozza emg hogy volt-e olyan döntö ahol a két csapat között a pont meghaladta az 50-et

vanEpontKul50tobb = False
for item in dontok:
    if item.pontKulonbseg() > 50:
        vanEpontKul50tobb = True
        break
if vanEpontKul50tobb:
    print("Igen volt megfelelő döntő ")
else:
    print("nem volt megfelelő döntö")
    print("----------------------------------------------------")


#minden eleme teljesiti
#haatározza meg hogy a meccsek nezoszama meghaladja a 70000-et
mindenEnezoszam70eTobb = True
for item in dontok:
    if not (item.nezoszam > 70000):
        mindenEnezoszam70eTobb = False
        break
if mindenEnezoszam70eTobb:
    print("Minden döntő teljesiti a feltételt ")
else:
    print("nem minden döntő teljesiti a feltételt ")
print("----------------------------------------------------")

 #kiválasztás tétele
 #!!!!!!!!!!!!!
 #határozza meg hogy a néző szám meghaladja a 100000-et
dontoNezoszam100Etobb = None
for item in dontok:
    if item.nezoszam > 100000:
        dontoNezoszam100Etobb = item
        break
if dontoNezoszam100Etobb != None:
    print("van ilyen döntöamely nézó száma: {dontoNezoszam100Etobb.nezoszam}")
else:
    print("nincs ilyen döntö")
    print("----------------------------------------------------")
#Keresés tétele
#!!!!!!!!!
#keresse meg az első olyan döntőt amely a csapatok pontjai között 10 külömbség
indexPontkul10 = None
for i in range(len(dontok)):
    if dontok[i].pontKulonbseg() == 10:
        indexPontkul10 = i
        break

if indexPontkul10 != None:
    print(f"Döntö:  {dontok[indexPontkul10]}, NÉZŐSZÁM: {dontok[indexPontkul10].nezoszam}")
else:
    print("Nincs megfelelő döntő")


    print("----------------------------------------------------")

#buborékos rendezés
#rendezze a döntöket pont külömbség alapján csökkenő sorrendbe
for i in range(len(dontok)-1, 0, -1):
    for j in range(i):
        if dontok[j].pontKulonbseg() < dontok[j+1].pontKulonbseg():
            dontok[j], dontok[j+1] =  dontok[j], dontok[j]
for item in dontok:
    print(item)