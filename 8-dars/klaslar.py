import datetime
import requests
from bs4 import BeautifulSoup

class ParsingWebsiteBase:

    def __init__(self, url) -> None:
        self.url = url
         
            
    def run(self):
        """
        Bu asosiy ishga tushiruvchi funksiya


        """
        file = f"news-{self.tartibsiz_sana()}"
        
        self.file_save(file)
        
        return "fayl saqlandi"
    
    def parsing(self):
        """
            Bu funksiya url qabul qiladi va text content qaytaradi
        """
        r = requests.get(self.url)
        content = BeautifulSoup(r.text, 'html.parser')

        for link in content.find_all('p'):
            return link.get_text()
    
    def file_save(self, fileName):
        """
            Bu funksiya fayl nomi va text qabul qiladi. textni faylga yozib beradi
        """
        with open(fileName, "w") as file:
            
            file.write(self.parsing())
        return "faylga saqlandi "
    
    def tartibsiz_sana(self):
        """
        Bu tartibsiz sana chiqaradigan funksiya
        """
        vaqt = str(datetime.datetime.now()).replace(':','-')
        return vaqt.replace('.','-')

    