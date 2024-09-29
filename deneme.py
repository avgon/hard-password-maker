import random

karakter ="£+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 

uzunluk = int(input("Kaç karakterlik bir şifre oluşturmak istersiniz"))


sifre = ""
for i in range(uzunluk):
    sifre = sifre + random.choice(karakter) 

print(sifre)