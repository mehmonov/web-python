from functions import salom
import requests

# *args - funksiyaga bir nechta qiymatlar olib kiroladi va ularni turi tuple bo'ladi
# **kwargs - funksiyaga lug'at ko'rinishida(kalit va qiymat) ma'lumot olib kiroladi
# kwargs - funksiya chaqirilganda lug'at ko'rinishida ma'lumot biriktiriladi

# user kitob va muallif kiritishi kerak
# user kiritgan kitobni funksiyada kalit va qiymatga ajratib bizga ko'rsatishi kerak


# kitobNomi = input("nomini kiriting: ")
# muallif = input("muallini kiriting: ")
    
# def kitoblar(**kitoblar):
#     for i, v in kitoblar.items():
#         for kitob, muallif in v.items():
#             print(f"{kitob} -- {muallif}")


# kitoblar(kitobNomi={kitobNomi:muallif})

while True:
    r= requests.get('https://www.w3schools.com/python/default.asp')

    print(r.text)