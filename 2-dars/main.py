# list - > ["info"]
# dict - > {'kalit': "qiymat"}

kitoblar = {
    'kitob1':{
        "muallif": "Muallif 1",
        "narx": 100
    },
    'kitob2':{
        "muallif": "Muallif 2",
        "narx": 200
    },
}
kitoblar["kitob4"] = {"muallif":"muallif 4", "narx": "400"}

for i in kitoblar:
    print(kitoblar[i]["muallif"])
    print(kitoblar[i]["narx"])
    # forni sharti tugaganidan keyin pastki qismdagi kodlarni o'qiydi 

# kitoblar.append("kitob444")
# print(kitoblar)

# userdan kitob so'raymiz. mavjud bo'lsa mavjud desin agar mavjud bo'lmasa userga savol bersin, "mavjud emas, yangi qo'shamizmi? " - > agar user ha deb yozsa, userdan kitobni mualligi va narxini so'rasin, va userdan olingan ma'lumotlarni lug'atga qo'shib qo'ysin va userga aynan o'sha elementni ko'rsatsin

# while True:
#     usermsg = input("Kitob nomi: ")
#     if usermsg  in kitoblar:
#         print('ok')
#         break
#     else:
#         ask = input("Kitob bizda mavjud emas, siz yangi kitob qo'shmoqchimisiz?")

#         if ask == 'ha':
#             kitoblar.append(usermsg)
#             print(kitoblar)
#         else:
#             print("hayr")
