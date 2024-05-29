kitoblar = {
    "kitob": {
        "muallif": "Muallif 1",
        "narx": 200,
    },
    "kitob2": {
        "muallif": "Muallif 2",
        "narx": 300,
    },
}

# def kitob_qidir(kitob):
#     if kitob in kitoblar:
#         print("bu kitob bizda bor")
#     else:
#         print("bu kitob bizda yo'q")


# kitob_qidir("kitob")

# topshiriq: sum ishlatmasdan umumiy qiymatni hisoblash kerak

# 1, 2 ,3 = > bir biriga qo'shish kerak


def sonlar(amal, *sonlar):
    
    quti = 0
    for i in sonlar:
        quti = quti + i
    print(quti)

ism  = input("user")
amal = input('amalni')
sonlar(amal, ism)


