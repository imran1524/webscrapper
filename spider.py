# Import Request module
import requests
from bs4 import BeautifulSoup

url = 'http://www.hot-dinners.com/Features/Articles/new-and-recently-opened-london-restaurants'

response = requests.get(url)
data = response.text
# print(data)

soup = BeautifulSoup(data,'html.parser')
links = soup.prettify()
