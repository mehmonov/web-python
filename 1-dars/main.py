# lug'atlar va to'plamlar
# dict va list


ism = input("ism: ")
yosh = input("yosh ")
kasb = input("kasb: ")
insonlar = {
    "Husniddin":{
        "yosh":20,
        "kasb":"dasturchi"
    }
} 
insonlar[ism] = {"yosh": yosh, "kasb": kasb}

print(insonlar)

