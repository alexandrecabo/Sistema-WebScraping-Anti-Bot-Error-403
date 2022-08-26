import cfscrape #pip install cfscrape
from bs4 import BeautifulSoup as bs

scraper = cfscrape.create_scraper()
response = scraper.get("https://www.idealista.pt/comprar-casas/porto/")

if response.status_code == 200:
    print(f'\n\nCodido: {response} | Acesso Autorizado\n\n')
else:
    print('Deu Ruim Mané!')
