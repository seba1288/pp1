import re

str = 'To be, or not to be, that is the question'

st = re.findall('[aeiouy]',str)
print(st)