import bs4
import requests

def get_amazon_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('<span class="a-color-base">a partir de R$208,92</span>')
    return elems[0].text.strip()


price = get_amazon_price('https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=17XFOP3A8285O&dchild=1&keywords=automate+boring+stuff+with+python&qid=1611411664&sprefix=automate+%2Caps%2C310&sr=8-1')
print('The price is: ' + price)
