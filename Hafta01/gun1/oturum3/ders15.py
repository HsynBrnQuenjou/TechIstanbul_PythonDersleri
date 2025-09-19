"""
Kullanıcıdan şu bilgileri alıp, ekrana güzel bir mesaj yazdırın:

Ad
Yaş
Şehir
Hobisi

"""

ad = input("Adunız: ")
yas = int(input("Yaşınız: "))
sehir = input("Yaşadığınız şehir: ")
hobi = input("Hoboniz: ")
boy = float(input("Boyunuz: "))
devam_durumu = bool(input("Devam durumunuz: ")) #Dolu veri -> True, Boş veri -> False

print("\n--- KİŞİSEL TANITIM KARTI ---")
print("İsim: ", ad)
print("Yaşınız: ", yas)
print("Yaşanıdığınız şehir: ", sehir)
print("Hobiniz: ", hobi)
print("Boyunuz: ", boy)
print("Devam durumunuz: ", devam_durumu)
print("-------------------------------")