#input() kullanıcıdan veri almak için kullanılan method

print("Adın nedir?")
ad = input() #input str() tipidir
print("Memnun oldum.", ad)
print(type(ad)) #str olacaktır

print("Yaşın kaç?")
yas = int(input())
print(yas * 2)