import requests
import time
from bs4 import BeautifulSoup
from collections import Counter
import os
from urllib.parse import urlparse
import colors
import logo
import webbrowser

URL = "https://www.acp.at/"
domain = URL.split("//")[1].split("/")[0]
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find the URL of the CSS file
css_link = None
for link in soup.find_all("link"):
    if link.get("rel") == ["stylesheet"]:
        css_link = link.get("href")
        break

if css_link is not None:
    # Check if the css link contains a whole url or not
    if "http" in css_link:
        css_url = css_link
    else:
        css_url = f"{URL}{css_link}"

    # Remove "//" except after "http" and "https"
    if "//" in css_url and not css_url.startswith("http://") and not css_url.startswith("https://"):
        css_url = css_url.replace("//", "/")

    # Get css content
    css_response = requests.get(css_url)
    css_content = css_response.content.decode()

    print("Extracting Colors from website ...")
    #Call the function to get the colors
    colors.extract_colors(URL, css_content)

    print("Loading image from website ...")
    #Call the function to get the logo
    logo_link = logo.extract_logo(domain)
    print("Logo successfully pulled")

    url = 'file:///C:/Users/leonw/OneDrive - HTL Villach/HTL/artiPHISHial/artiPHISHial/cssscraper/login.html'

    # Set the browser to use
    os.environ['BROWSER'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    # Open the URL in the specified browser
    webbrowser.open(url)
