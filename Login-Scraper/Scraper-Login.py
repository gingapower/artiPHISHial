from cgitb import text
from cmath import log
from bs4 import BeautifulSoup
import requests
import re
import os


url = "https://www.w3schools.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify()) #print HTML

with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))

#print(doc)

#login = doc.find_all(string="Sign in") #find gives first result
#links = doc.find_all(["a"],text="Sign in")
#print(login)
#parent = login[0].parent
#print(parent)
#print(links)

links_with_text = []
for a in doc.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
a = doc.find_all('a')


#search for Login String in all hrefs:
check_login = [x for x in links_with_text if "login" in x]
if not check_login:
    print('Word: Login no found')
    #search for all SignIn Strings in all hrefs:
    check_log_in = [x for x in links_with_text if "log-in" in x]
    if not check_log_in:
        print('Word: Log-in not found')
        check_SignIn = [x for x in links_with_text if "SignIn" in x]
        if not check_SignIn:
            print('Word: SignIn not found')
            #Search for String SignIn in the hole HTML-file:
            search_word = 'SignIn'
            file_path = 'output.html'
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            search = ""
            for i, line in enumerate(lines):
                if search_word in line:
                    search = line
                    print(line)
                    #print(f'"{search_word}" found in line {i+1}: {line}')
                    for url in re.findall('"(/[^"]*)"', line):
                        if url.startswith('/'):
                            print('found Url:' +url)
                        
        else:   
            print(check_SignIn)
    else:
        print(check_log_in)
else:
    print(check_login)
        