#Scraping Numbers from HTML using BeautifulSoup
#Using Python to Access Web Data Week 4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
numlist = list()

for tag in tags:
    numlist.append(int(tag.contents[0]))

print('Count',len(numlist))
print('Sum',sum(numlist))
