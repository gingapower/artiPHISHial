import os
import re
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import htmlediter

def download_website(url):
    # Create a folder to store the downloaded files
    folder_name = urlparse(url).netloc
    os.makedirs(folder_name, exist_ok=True)

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
    for css_url in css_urls:
        absolute_url = urljoin(url, css_url)
        response = requests.get(absolute_url)
        css_filename = os.path.basename(css_url.split('?')[0])
        with open(os.path.join(folder_name, css_filename), 'w', encoding='utf-8') as f:
            f.write(response.text)

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
            urlretrieve(absolute_url, os.path.join(folder_name, image_filename))
    except Exception as e:
        print(f"An error occurred while image file: {e}")

    

    # Save the HTML of the webpage to a file in the folder
    try:
        with open(os.path.join(folder_name, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception as e:
        print(f"An error occurred while writing the HTML file: {e}")
    try:
        check_html(folder_name)
    except Exception as e:
        print(f"An error occurred while writing the HTML file: {e}")

def check_html(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            print(filename)
    htmlediter.insert_css_links(folder_path)


