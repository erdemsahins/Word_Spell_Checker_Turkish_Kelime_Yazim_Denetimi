"""

@Author Erdem Şahin 1160505041
Derlem TDK dan çekilmiştir. ilgili link https://sozluk.gov.tr/autocomplete.json şöyledir.
Alınan verilerin otomatik olarak düzenlenmesi ve txt formatında kayıt edilmesi için Derlem_Sozluk_Olusustur.py dosyasını kullanabilirsiniz.
Yazim denetimi yapmak için SequenceMatcher algoritması kullanarak her bir kelime aranan sonucla kıyaslanmaktadır.
Kıyaslama sonucunda elde edilen satır ID sinden kullanıcıya cevap dendürülür.

"""

import difflib
import heapq
import operator

# kullanıcıdan yazım denetimi yapılmak üzere veri alınır.
question = input("Lütfen yazımını düzeltmek istediğiniz kelimeyi giriniz: ")
# alınan veri küçük harf olacak şekilde düzenlenir.
question = question.lower()

# Derlemin dosya yolu tanımlanır.
DosyaYolu = 'Sözlük_Kelime_Listesi.txt'
distances = {}
key = []

with open(DosyaYolu, encoding="UTF-8") as dosya:
    satir = dosya.readline()
    print("\nBu işlem biraz uzun sürebilir. Lütfen Bekleyiniz...\nKarşılaştırma yapılıyor.")
    i = 0
    while satir:
        i=i+1
        distances[i] = 0
        # Derlem satır satır okunur.
        satir = dosya.readline()
        satir = str(satir).lower()
        # Alınan veri SequenceMatcher Alg ile Derlemdeki verilere kıyayaslanır.
        s = difflib.SequenceMatcher(lambda x: x == " ", question, satir)
        d = round(s.ratio(), 3)
        if distances[i] < d:
            distances[i] = d

    # Kayıt edilen oranlar sıralanarak en yüksek iki değer değişkene atanır.
    enYuksekİkiDeger = heapq.nlargest(2, distances.items(), key=operator.itemgetter(1))
    key = enYuksekİkiDeger

# Dosya tekrar açılarak cevap kullanıcıya dönderilir.
with open(DosyaYolu, encoding="UTF-8") as dosya:
    data = dosya.readlines()
    print("\nEn yüksek değer: "+ data[key[0][0]] + "En yüksek ikinci değer: "+ data[key[1][0]])
