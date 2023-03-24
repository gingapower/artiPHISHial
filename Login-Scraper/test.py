import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve

# URL of the webpage to download
url = 'https://www.apple.com/us/shop/goto/account'

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
for img in soup.find_all('img'):
    image_url = img.get('src')
    if image_url:
        image_urls.append(image_url)

# Download the images and save them to the folder
for image_url in image_urls:
    absolute_url = urljoin(url, image_url)
    image_filename = os.path.basename(image_url)
    urlretrieve(absolute_url, os.path.join(folder_name, image_filename))

# Save the HTML of the webpage to a file in the folder
with open(os.path.join(folder_name, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)