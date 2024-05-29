from scraping import  url_parsing
from file import file_write
import datetime
import random

def tartibsiz_son():   
    while True:
        nson = random.getstate()
        t_son = random.choice(nson)

        if t_son == 3 or t_son == None or type(t_son) == int :
            continue
        else:
            son = random.choice(t_son)
            return son
        
        
def tartibsiz_sana():
    vaqt = str(datetime.datetime.now()).replace(':','-')
    return vaqt.replace('.','-')
url = input("url kiriting: ")
def main(url):
    text = url_parsing(url)
    file_name = tartibsiz_sana()
    file_write(f"news-{file_name}", text)
    
    print("Tugallandi")
    
main(url)

