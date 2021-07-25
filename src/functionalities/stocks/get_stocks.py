from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_stocks_value(stocksSymbols: list):
  url = 'https://valorinveste.globo.com/cotacoes/'
  
  result = urlopen(url).read()
  soup = BeautifulSoup(result, 'html.parser')

  html_stocks = soup.find('table').find_all('tr')

  """
    Para cada 'tr', possui:

    - Nome do ativo
    - Código
    - Última cotação
    - Variação
    - Fechamento
  """

  stocks: list = []

  for s in html_stocks:
    try:
      tds = s.find_all('td')
      
      symbol = tds[1].text.strip()
    
      if symbol in stocksSymbols:
        value = float(tds[3].text.replace('%', '').strip().replace(',', '.'))

        stocks.append((symbol, value))

    except IndexError as e:
      pass

  return stocks

if __name__ == '__main__':
  get_stocks_value(['ABEV3'])