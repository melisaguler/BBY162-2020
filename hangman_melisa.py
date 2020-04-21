# adam asmaca programındada kullanılacak değişkenleri olusturdum.
kelime = "evdekal"
cizgi = len(kelime) * "_"
list_cizgi = []
list_kelime = []
can = 3

for i in cizgi:
    list_cizgi.append(i)
for i in kelime:
    list_kelime.append(i)

print("""Sevgili arkadaslar Adam Asmaca Oyununa Hoşgeldiniz Toplam 3 Can Hakkınız vardır.
Tahmin Girişlerinizi Küçük Harf Olarak Yapınız""")

# can bittiğinde oyununda bitmesi için while döngüsü olusturdum.
while (can != 0):
    flag = False
    print("can :", can)

    # döngü her başa döndüğünde oyuncuya kelime tablosunu göstermek için for döngüsünü kullandim..
    for i in list_cizgi:
        print(i, "\n")

    tahmin = input("\nbir harf giriniz : ")
    print()

    # kelime değişkeninde karakterleri index ve value olacak şekilde ayrılması
    for index, value in enumerate(kelime):

        # girilen harf doğru ise oyuncuya gösterilen tabloyu günceller
        if kelime[index] == tahmin:
            list_cizgi[index] = value
            flag = True

    # girilen harf yanlış ise, canı 1 azaltır
    if (flag == False):
        print("bilemediniz:(\n")
        can -= 1

    if (can == 0):
        print("oyun bitti KAYBETTİNİZ:(\n")

    # kelime tamamlanınca oyunu bitirmek için
    if (list_cizgi == list_kelime):
        print("evdekal\n")
        print("TEBRİK EDERİM kelimeyi buldunuz!!!")
        break