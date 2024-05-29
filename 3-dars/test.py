
while True:
    usermsg = input("Kitob nomi: ") # yangi kitob
    if usermsg  in kitoblar:
        print(f'Bu kitob mavjud. Muallif: {kitoblar[usermsg]["muallif"]} Narx:{kitoblar[usermsg]["narx"]}  ' )
        break
    else:
        ask = input("kitob mavjud emas, yangi qo'shamizmi?")
        
        if ask =="ha":
            muallif = input("Yangi kitobni muallifini kiriting")
            narx = input("Yangi kitobni narxini kiriting")
            
            kitoblar[usermsg] = {"muallif": muallif, 'narx': narx} # yangi kitob hosil qilish
            
            print(kitoblar)
            break
        else:
            break