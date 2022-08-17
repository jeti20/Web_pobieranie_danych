from bs4 import BeautifulSoup
from requests import get

#https://www.youtube.com/watch?v=CEOTrWowqfo

URL = 'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/warszawa/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('a', class_='css-1bbgabe'):
    footer = offer.find('p', class_='css-p6wsjo-Text eu5v0x0').get_text().strip().split('-')[0]
    title = offer.find('h6').get_text().strip()
    price = (offer.find('p', class_='css-wpfvmn-Text eu5v0x0').get_text().strip())
    link = offer.find('a')

    print(offer['href'], price)




