from cgitb import text
from cmath import log
from turtle import pos
from bs4 import BeautifulSoup
import requests
import re
import os


url = "https://www.instagram.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify()) #print HTML

with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))


links_with_text = []
for a in doc.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
a = doc.find_all('a')



poss_var = ["Login","login","LOGIN","Log-in","log-in", "Logon", "SignIn", "Sign-In"]
for var in poss_var:
    check = [x for x in links_with_text if var in x]
    if check:
        print(check)
    else:
        print(var + " not found!")

print(len(check))
if len(check) == 0:
    search_word = 'login'
    file_path = 'output.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        search = ""
        for i, line in enumerate(lines):
            if search_word in line:
                search = line
                #print(line)
                #print(f'"{search_word}" found in line {i+1}: {line}')
                for url in re.findall('"(/[^"]*)"', line):
                    if url.startswith('/'):
                        print('found Url:' +url)


        