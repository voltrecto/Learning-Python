#Extracting Data from JSON
#Using Python to Access Web Data Week 6

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc = input('Enter location: ')
print('Retrieving',loc)
data = urllib.request.urlopen(loc, context=ctx).read()
stuff = json.loads(data)
total = list()

for item in stuff['comments']:

    num = item['count']
    inum = int(num)
    total.append(inum)

print('Count:',len(total))
print('Sum:',sum(total))
