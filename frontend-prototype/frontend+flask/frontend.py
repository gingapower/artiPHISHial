from flask import Flask, send_from_directory, request, render_template
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
import shutil

app = Flask(__name__)




@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['myInput']
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
    mainhtml.find_links(doc, links_with_text)
    print(colored("Start to clone Loginpage!","blue"))
    clone.download_website(url, 1)
    screenshot.take_screenshot(url, 'screenshot.png',10)
    
    folder_path = cwd+ "\\" + "websites\\"+urlparse(url).netloc+"\\index.html"
    print(folder_path)
    screenshot.take_screenshot(folder_path, 'screenshot2.png', 4)
    screensho1_path = os.path.join(cwd, 'screenshot.png')
    screensho2_path = os.path.join(cwd, 'screenshot2.png')
    frontend = cwd + "\\static"
    shutil.copy(screensho1_path,frontend+"\\screenshot.png")
    shutil.copy(screensho2_path,frontend+"\\screenshot2.png")
        
    return render_template('screenshot.html')

if __name__ == '__main__':
    app.run()
