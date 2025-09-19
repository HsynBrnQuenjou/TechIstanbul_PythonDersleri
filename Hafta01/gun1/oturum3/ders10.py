#değişkenler ve veri tipleri
#değişken tanımlama kuralları
#1. harf veya _ iile başlamalı
#2. sayı ile başlayamaz
#3. türkçe karakter kullanılmaz (kullanılmamalı farklı sistemlerde sorun oluşturabilir)
#4. boşluk kullanılamaz
#5. özel karakter kullanılamaz -> _ harici
#6. büyük küçük harf duyarlılığı vardır
#7. anahtar kelimeler kulanılmaz (for not if elif while.... gibi)
#değişken tanımlama

# değişken = değer
# değer atama işlemi sağdan sola doğrudur
# atama işlemi için = kullanılır
# değişken isimleri anlamlı olmalıdır
# bir değişkene atanan değer istediğimiz zaman değiştirilebilir

ad = "TechIstanbul"
print(ad)
print(type(ad)) #str
tip = type(ad)
print(tip) #str
sayi = 5
print(sayi) #5
print(type(sayi)) #int
print(sayi == 8) #false
print(sayi * 2) #10