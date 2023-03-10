from cmath import log
from pickle import FALSE
from turtle import pos
from bs4 import BeautifulSoup
import requests
import re
import os


url = "https://microsoft.com"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#print(doc.prettify()) #print HTML
#wirte html output in file:
with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))

#find all links with href in it:
links_with_text = []
for a in doc.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
a = doc.find_all('a')
#print(links_with_text)


#check if for <form> fied
def check_form():
    form = doc.find_all("form")
    print(form)
    for i in form:
        if i.find_all("input"):#check if input field in form
            print("input found")
check_form()

#check all links on page
check = []
def check_links(linklist):
    poss_var = ["Login","login","LOGIN","Log-in","log-in", "Logon", "LOGON", "Log-on", "logon", "SignIn", "Sign-In","sing-in", "Accounts", "accounts", "account"]
    for var in poss_var:
        check = [x for x in linklist if var in x]
        if check:
            print(check)
        
check_links(links_with_text)

#check complete html - search keywords

check_url = False
print(len(check))
if len(check) == 0:
    file_path = 'output.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        search = ""
        for i, line in enumerate(lines):
            if "href" in line:
                matches = re.findall(r'href="(.+?)"', line)
                check_links(matches)
            #build for loop in:          
            if "login" in line:
                search = line
                print(line)
                for url in re.findall('"(/[^"]*)"', line):
                    if url.startswith('/'):
                        check_url = True
                        print('found Url:' +url)

#check if it has a google Login (Googl -services:)

file_path = 'output.html'
if check_url == False:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "https://accounts.google.com/" in line:
                print("Google Login found")
                print("url: https://accounts.google.com/")


#def clonewebpage ():
        