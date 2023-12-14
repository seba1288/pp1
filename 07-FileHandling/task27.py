import re

str = 'To be, or not to be, that is the question'

st = re.findall('\s',str)
print(st)
print(len(st)+1)