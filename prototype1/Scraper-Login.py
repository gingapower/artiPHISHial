from cmath import log
from doctest import ELLIPSIS_MARKER
from pickle import FALSE
from turtle import pos
from bs4 import BeautifulSoup
from urllib import request
import requests
import re
import clonetry1
import screenshot
import maincss 


#Vars
poss_var = ["Login","login","LOGIN","sign_in","Sign_in","log_in","Log_in","Log-in","log-in","signin", "Logon", "LOGON", "Log-on", "logon", "SignIn", "Sign-In","sing-in", "Accounts", "accounts", "account","Account","client","signup"]
links_with_text = []
check = []
login_link = []
url = input("pls enter the fucking url")
#url="https://github.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#wirte html output in file:
with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))

#find all links with href in it:
def find_links():
    for a in doc.find_all('a', href=True): 
        if a.text: 
            links_with_text.append(a['href'])
    a = doc.find_all('a')
    print(links_with_text)

#find <a> with clear title
def find_links_title():
    for link in doc.find_all('a'):
        title = link.get('title')
        if title is not None and any(var.lower() in title.lower() for var in poss_var):
            href = link.get('href')
            login_link.append(href)
            return True

#check if for <form> fied
def check_form(document):
    poss_vars = ["username", "e-mail", "email", "mail", "USERNAME", "Account","Password", "password", "secret"]
    for var in poss_vars:
        if document.find('input', {'name'.lower(): "email"} and {'name'.lower():'password'}): 
            return True
        
#check all links on page
def check_links(linklist):
    found_var = False
    for var in poss_var:
        for x in linklist:
            if var in x:
                login_link.append(x)
                found_var = True
    if found_var:
        return True
    else:return False
        
#check complete html - search keywords
def check_html():
    #print(len(check))
    if len(check) == 0:
        file_path = 'output.html'
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "href" in line:
                    matches = re.findall(r'href="(.+?)"', line)
                    #print(matches)
                    check_links(matches)
                                          
                if "login" in line:
                    search = line
                    #print(line)
                    for url in re.findall('"(/[^"]*)"', line):
                        if url.startswith('/'):
                            login_link.append(url)
                            return True
                       

#check if it has a google Login (Googl -services:)
def check_google_login():
    file_path = 'output.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "https://accounts.google.com/" in line:
                print("Google Login found")
                print("url: https://accounts.google.com/")

def test():
    for i in poss_var:
        url2 = url+i
        #print(url2)
        result2 = requests.get(url2).text
        doc2 = BeautifulSoup(result, "html.parser")
        check_form(doc2)
        
def buildurl(linklist, url):
    for index, element in enumerate(linklist):
        if element.startswith("/"):
            if url.endswith("/"):
                url = url[:-1]
            newurl = url + element
            linklist[index] = newurl
            #linklist.remove(element)

def main():
    find_links()
    if(check_form(doc)):
        print("Page identified as Loginpage!")
        clonetry1.download_website(url)
        screenshot.take_screenshot(url, 'screenhot.png')
    else:  
        print("checking all found links:")   
        print(check_links(links_with_text))#
        print("titles of the links:")
        print(find_links_title())
        print("checking html code:")
        print(check_html())
        print("check if google login:")
        print(check_google_login())
        # print("checking standart ednings:")
        # test()
        #print(login_link)
        if len(login_link) > 0:
            buildurl(login_link, url)
            print(login_link)
            #clonetry2.clone_webpage(login_link[0])
            clonetry1.download_website(login_link[0])
            screenshot.take_screenshot(login_link[0], 'screenhot.png')
            # Specify the file path to your HTML file
    
    maincss.main(url)

main()