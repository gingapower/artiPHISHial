import requests
from bs4 import BeautifulSoup
from collections import Counter
import os.path
from urllib.parse import urlparse
import colors
URL = "https://www.instagram.com/"
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

    colors.extract_colors(css_content)

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
else: 
    print("CSS file link not found")

#TO DO: Scale options for Logo
#TO DO: List the first 4 top colors of the website