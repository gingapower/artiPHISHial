from cgitb import text
from cmath import log
from bs4 import BeautifulSoup
import requests


url = "https://www.microsoft.com/en-au/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify()) #print HTML

login = doc.find_all(string="Sign in")

parent = login[0].parent
tbody = doc.tbody

print(tbody)
#print(parent)