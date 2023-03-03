import requests
import time
import re
from bs4 import BeautifulSoup
from collections import Counter
import os.path
from urllib.parse import urlparse

URL = "https://www.addit.at/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#with open('output.html', 'w', encoding="utf-8") as file:
#    file.write(str(soup))

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

    # Extract the hex color values from the CSS file
    color_regex = re.compile(r"#([0-9a-fA-F]{6})")
    color_matches = color_regex.findall(css_content)


    if color_matches:
        print("Hexadecimal color codes found in the CSS file:")
        time.sleep(2)
        
        # Count the frequency of each color
        color_counts = Counter(color_matches)
        
        # Print the top colors
        print("Most common colors:")
        for color, count in color_counts.most_common(10):
            print(f"{color}: {count}")
            
        print("-----Done-----")
    else:
        print("Color not found")
else:
    print("CSS file not found.")

# Find the URL of the logo image
logo_link = None
for img in soup.find_all("img"):
    if ("logo" or "title") in img.get("src"):
        logo_link = img.get("src")
        break

if logo_link is not None:
    # Download the logo image
    if "http" in logo_link:
        logo_url = logo_link
    else:
        logo_url = f"{URL}/{logo_link}"

    logo_response = requests.get(logo_url)

    if logo_response.ok:
        # Save the logo image with the original image format
        logo_filename = os.path.basename(urlparse(logo_url).path)
        with open(logo_filename, "wb") as f:
            f.write(logo_response.content)
        print(f"Logo image downloaded successfully and saved as {logo_filename}")
    else:
        print("Failed to download logo image")
else:
    print("Logo image not found")
