# Import Request module
import requests

url = 'http://www.hot-dinners.com/Features/Articles/new-and-recently-opened-london-restaurants'

response = requests.get(url)
data = response.text
# print(data)