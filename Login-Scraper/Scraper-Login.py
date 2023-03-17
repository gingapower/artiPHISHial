from cmath import log
from pickle import FALSE
from turtle import pos
from bs4 import BeautifulSoup
from urllib import request
import requests
import re

#Vars
poss_var = ["Login","login","LOGIN","Log-in","log-in", "Logon", "LOGON", "Log-on", "logon", "SignIn", "Sign-In","sing-in", "Accounts", "accounts", "account","Account","client"]
links_with_text = []
check = []
url = "https://digi4school.at/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#wirte html output in file:
with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))


def find_links():
    #find all links with href in it:
    for a in doc.find_all('a', href=True): 
        if a.text: 
            links_with_text.append(a['href'])
    a = doc.find_all('a')
    #print(links_with_text)


#check if for <form> fied
def check_form(document):
    poss_var = ["username", "e-mail", "email", "mail", "USERNAME", "Account","Password", "password", "secret"]
    for var in poss_var:
        if document.find('input', {'name': var}):
            return("found: "+var)
        

#check all links on page
def check_links(linklist):
    for var in poss_var:
        for x in linklist:
            if var in x:
                return(x)
        
#check complete html - search keywords
check_url = False
def check_html():
    #print(len(check))
    if len(check) == 0:
        file_path = 'output.html'
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            search = ""
            for i, line in enumerate(lines):
                if "href" in line:
                    matches = re.findall(r'href="(.+?)"', line)
                    check_links(matches)
                          
                if "login" in line:
                    search = line
                    #print(line)
                    for url in re.findall('"(/[^"]*)"', line):
                        if url.startswith('/'):
                            check_url = True
                            return(url)

#check if it has a google Login (Googl -services:)
def check_google_login():
    file_path = 'output.html'
    if check_url == False:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "https://accounts.google.com/" in line:
                    print("Google Login found")
                    print("url: https://accounts.google.com/")

def test():
    for i in poss_var:
        url2 = url+i
        print(url2)
        result2 = requests.get(url2).text
        doc2 = BeautifulSoup(result, "html.parser")
        print(check_form(doc2))
        
    
def main():
    find_links()
    print("standart Loginpage: ")
    print(check_form(doc))    
    print("check Links: ")
    print(check_links(links_with_text))
    print("check HTML: ")
    print(check_html())
    check_google_login()
    test()


main()