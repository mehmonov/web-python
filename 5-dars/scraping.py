import requests
from bs4 import BeautifulSoup

def url_parsing(url): 
    """
        Bu funksiya url qabul qiladi va text content qaytaradi
    """
    r = requests.get(url)
    content = BeautifulSoup(r.text, 'html.parser')

    for link in content.find_all('p'):
        return link.get_text()
    
