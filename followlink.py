#Following Links in Python
#Using Python to Access Web Data Week 4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
pos = input('Enter position: ')
scount = int(count)
spos = int(pos)
counter = 0

while counter < scount:
    pcounter = 0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if pcounter < spos-1:
            pcounter += 1
            continue
        else:
            print('Retrieving:',tag.get('href', None))
            break
    url = tag.get('href', None)
    counter += 1
