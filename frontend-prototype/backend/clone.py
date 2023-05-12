import os
import re
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import htmledit
from termcolor import colored

def download_website(url, method):
    # Create a folder to store the downloaded files
    folder_name = urlparse(url).netloc
    cwd = os.getcwd()
    folder_path = cwd+ "\\" + "websites\\"+folder_name
    os.makedirs(folder_path, exist_ok=True)

    # Download the HTML of the webpage
    response = requests.get(url)
    html = response.text

    # Extract the CSS URLs from the HTML
    soup = BeautifulSoup(html, 'html.parser')
    css_urls = []
    for link in soup.find_all('link', rel='stylesheet'):
        css_url = link.get('href')
        if css_url:
            css_urls.append(css_url)

    # Download the CSS files and save them to the folder
    try:
        for css_url in css_urls:
            absolute_url = urljoin(url, css_url)
            response = requests.get(absolute_url)
            css_filename = os.path.basename(css_url.split('?')[0])
            with open(os.path.join(folder_path, css_filename), 'w', encoding='utf-8') as f:
                f.write(response.text)
    except Exception as e:
        print(colored(f"Error occurred while downloading css: {e}","red"))

    # Extract the image URLs from the HTML
    image_urls = []
    try:
        for img in soup.find_all('img'):
            image_url = img.get('src')
            if image_url:
                image_urls.append(image_url)
        # Download the images and save them to the folder
        for image_url in image_urls:
            absolute_url = urljoin(url, image_url)
            image_filename = os.path.basename(image_url)
            image_filename = re.sub('[^0-9a-zA-Z_\-\.]', '_', image_filename) # replace invalid characters with an underscore
            urlretrieve(absolute_url, os.path.join(folder_path, image_filename))
    except Exception as e:
        print(colored(f"An error occurred while downloading image file: {e}","red"))

    

    # Save the HTML of the webpage to a file in the folder
    try:
        with open(os.path.join(folder_path, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception as e:
        print(colored(f"An error occurred while writing the HTML file: {e}","red"))
    try:
        check_html(folder_name, method)
    except Exception as e:
        print(colored(f"An error occurred while edeting the HTML file: {e}","red"))

def check_html(folder_path, method):
    htmledit.insert_css_links(folder_path, method)


