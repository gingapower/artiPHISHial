from cmath import log
from doctest import ELLIPSIS_MARKER
from pickle import FALSE
from turtle import pos
from bs4 import BeautifulSoup
import itertools
from urllib import request
import requests
import re
import clonetry1
import screenshot
import maincss 


#Vars
link_var = []
input_mail=[]
input_pass=[]
with open('link_keywords', 'r', encoding='utf-8') as file:
    for line in file:
        link_var.append(line.strip())
with open('mail_keywords', 'r', encoding='utf-8') as file:
    for line in file:
        input_mail.append(line.strip())
with open('password_keywords', 'r', encoding='utf-8') as file:
    for line in file:
        input_pass.append(line.strip())


links_with_text = []
check = []
login_link = []
uniquestrings = []
finallinks = []
url = input("pls enter a url: ")
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
        if title is not None and any(var.lower() in title.lower() for var in link_var):
            href = link.get('href')
            login_link.append(href)
            return True

#check if for <form> fied
def check_form(document, list1, list2):
    for var1, var2 in itertools.product(list1, list2):
        if document.find('input', {'name'.lower(): var1}) and document.find('input', {'name'.lower(): var2}):
            return True
            
        
#check all links on page
def check_links(linklist):
    found_var = False
    for var in link_var:
        for x in linklist:
            if var in x.lower():
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
                    check_links(matches)
                                          
                if "login" in line:
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
                return True
    return False
                
        
def buildurl(linklist, url):
    for index, element in enumerate(linklist):
        if element.startswith("/"):
            if url.endswith("/"):
                url = url[:-1]
            newurl = url + element
            linklist[index] = newurl
            #linklist.remove(element)

def sortlinks(linklist, unique_strings):
    for string in linklist:
        if string not in unique_strings:
            unique_strings.append(string)
    linklist[:] = unique_strings

def filter_links(links, list):
    keyword_list = ["signup", "login"]
    
    for link in links:
        for keyword in keyword_list:
            if keyword in link:
                list.append(link)
                break  # Stop checking other keywords for this link

    return list


def main():
    find_links()

    if(check_form(doc, input_mail, input_pass)):
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
        if(check_google_login()):
            print("Google Login found")
            print("url: https://accounts.google.com/")
            clonetry1.download_website("https://accounts.google.com/")
            screenshot.take_screenshot("https://accounts.google.com/", 'screenhot.png')
        elif len(login_link) > 0:
            buildurl(login_link, url)
            sortlinks(login_link, uniquestrings)
            filter_links(uniquestrings, finallinks)
            
            print(finallinks)
            clonetry1.download_website(finallinks[0])
            screenshot.take_screenshot(finallinks[0], 'screenhot.png')
    
    maincss.main(url)

main()