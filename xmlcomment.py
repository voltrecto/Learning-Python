#Extracting Data from XML
#Using Python to Access Web Data Week 5

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc = input('Enter location: ')
print('Retrieving',loc)
data = urllib.request.urlopen(loc, context=ctx).read()

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
total = list()

for item in lst:
    num = item.find('count').text
    inum = int(num)
    total.append(inum)

print('Count:',len(total))
print('Sum:',sum(total))
