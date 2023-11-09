"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""



import requests
import re

def fn_RemoveHTML(sentence) :
	sentence = re.sub('(<([^>]+)>)', '', sentence)
	return sentence

req = requests.get('https://sd.deltasd.bc.ca')
data = req.text
#print(data)

data1=fn_RemoveHTML(data)
print(data1)





"""from tkinter import *
from tkhtmlview import HTMLLabel
import requests
import re
import json
import urllib.request"""


"""data = requests.get('https://sd.deltasd.bc.ca')
#print(data.text)

data1 = data.text
data1=json.dumps(data1)
data1=json.loads(data1)

html1 = re.compile('<>')
string1=re.sub(html1, '', data1)

print(string1)

#<.*?>"""
