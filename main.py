import requests
import string
from bs4 import BeautifulSoup

Enter_input = input("Search: ")
u_i = string.capwords(Enter_input)
list = u_i.split()
word = "_".join(list)

url = "https://en.wikipedia.org/wiki/" + word

def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')  # Ganti 'html.pars' menjadi 'html.parser'
    details =  soup.find('table', {'class': 'infobox vcard'})  # Menggunakan 'find' untuk mencari satu elemen
    if details is not None:
        h = details.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading and detail:  # Periksa apakah heading dan detail tidak kosong
                for x, y in zip(heading, detail):
                    print("{} :: {}".format(x.text.strip(), y.text.strip()))  # Hapus spasi ekstra
                    print("---------------------------------")

    for i in range(1, 3):
        paragraphs = soup.find_all('p')  # Menggunakan 'find_all' untuk mencari semua paragraf
        if i < len(paragraphs):
            print(paragraphs[i].text.strip())  # Hapus spasi ekstra

wikibot(url)
