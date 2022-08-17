from requests import get
from json import loads
from terminaltables import  AsciiTable

#https://www.youtube.com/watch?v=ks6C3VWzT4M

CITIES = ['Poznań']
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop/'
    response = get(url)

    #tworzenie tabelki, nazwy kolumn
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]
    wyszukuje i wpisuje wartości w rekordy
    for row in loads(response.text): #loads sprawia, że plik z json który jest wyświetlany jako string, wyświetlany jest jako słownik dzieki czemu mzoemy wybrać z niego np. miejscowość
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])
    table = AsciiTable(rows)
    print((table.table))

if __name__ == '__main__': #sprawdza czy __name__ to name
    main() #wywołuje funkcję