def file_write(file_name, text):
    """
        Bu funksiya fayl nomi va text qabul qiladi. textni faylga yozib beradi
    """
    with open(file_name, "w") as file:
        
        file.write(text)
    return "faylga saqlandi "
    
