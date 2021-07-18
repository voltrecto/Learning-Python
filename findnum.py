#Finding Numbers in a Haystack
#Using Python to Access Web Data Week 2

import re

txtdata = open('regex_sum_1301278.txt')
numlist = list()
for line in txtdata:
    line = line.rstrip()
    txtsearch = re.findall('[0-9]+', line)
    for value in txtsearch:
        num = int(value)
        numlist.append(num)

print('Count:',len(numlist))
print('Sum:',sum(numlist))
