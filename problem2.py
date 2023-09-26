"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""
import requests
import re
data = requests.get('https://sd.deltasd.bc.ca',timeout=None)
#print(data.text)

data1 = data.text

html1 = re.compile('<>')
string1=re.sub(html1, '', data1)

print(string1)

#<.*?>
