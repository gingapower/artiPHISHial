from cgitb import text
from cmath import log
from bs4 import BeautifulSoup
import requests


url = "https://www.microsoft.com/en-au/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify()) #print HTML

#print(doc)

login = doc.find_all(string="Sign in") #find gives first result
#links = doc.find_all(["a"],text="Sign in")
print(login)
parent = login[0].parent
print(parent)
#print(links)

links_with_text = []
for a in doc.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])

#print(links_with_text)

for i in links_with_text:
    if 'SignIn' in i:
        print(f"The word 'Sign' is found in link: {i}")


login_link = doc.find('a', {'class': 'SignIn'})
if login_link is not None:
    print(f"Found login link: {login_link['href']}")
else:
    print("No login link found.")
#tbody = doc. 

#print(login)
#print(parent)