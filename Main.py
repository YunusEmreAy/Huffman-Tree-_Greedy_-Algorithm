# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com

with open("Main.txt", "r", encoding="utf-8") as file:

    print("Main.txt Dosyasında Bulunan Metin:")
    print("------------------------------------------------------------")
    metin = file.read()
    yeni_metin = ''
    for i in range(0,len(metin),8):
        yeni_metin+= metin[i:i+8]
        yeni_metin += ' '

    string_metin = ''.join([chr(int(a, 2)) for a in yeni_metin.split()])
    print(string_metin)
    print("------------------------------------------------------------")

frekans = dict()
for i in string_metin:
    if i not in frekans:
        frekans[i] = 1
    else:
        frekans[i] +=1
print("\nHarflerin Frekanslari:",frekans)

Elemanlar = list()
for anahtar,tekrar in frekans.items():
    temp = list()
    temp.append(anahtar)
    temp.append(int(tekrar))
    Elemanlar.append(temp)

for i in range(len(Elemanlar) - 1):
    for j in range(0, len(Elemanlar) - i - 1):
        if Elemanlar[j][1] > Elemanlar[j + 1][1]:
            temp = Elemanlar[j]
            Elemanlar[j] = Elemanlar[j + 1]
            Elemanlar[j + 1] = temp

while len(Elemanlar)!=1:
    liste = list()
    Elemanlar[0].append(0)
    Elemanlar[1].append(1)
    liste.append(Elemanlar[0])
    liste.append(Elemanlar[1])
    liste.append(Elemanlar[0][-2]+Elemanlar[1][-2])
    Elemanlar.append(liste)
    del Elemanlar[0]
    del Elemanlar[0]


son_sozluk = dict()
temp = ""
def bit_belirleme (liste):
    global temp
    if type(liste[0]) == str:
        son_sozluk[liste[0]] = temp
        return

    else:
        temp += "0"
        bit_belirleme(liste[0])
        temp = temp[0:-1]

        temp += "1"
        bit_belirleme(liste[1])
        temp = temp[0:-1]


bit_belirleme(Elemanlar[0])


print("\nHarflerin Bitleri: ",son_sozluk)

son_bit = 0
for harf,bit in son_sozluk.items():
    son_bit += (frekans[harf] * len(bit))


print("\nTXT Dosyasındaki Girdinin Boyutu: {} Byte".format(len(metin)))
print("SIKISTIRILMIS Girdinin Boyutu: {} Byte".format(son_bit))
