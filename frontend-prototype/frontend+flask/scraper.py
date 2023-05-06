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

#Functions
def main(url):
    

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
    clone.download_website(url)
    screenshot.take_screenshot(url, 'screenhot.png')
#check if input field
