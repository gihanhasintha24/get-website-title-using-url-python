# how to print website title using url

from bs4 import BeautifulSoup
import requests
url = input('enter url : ')
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
print(soup.title)