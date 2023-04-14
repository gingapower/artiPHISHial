import requests
from PIL import Image
from io import BytesIO
import re
from bs4 import BeautifulSoup

def extract_logo(query):
    try:
        # Call clearbit API to get the logo image
        response = requests.get(f"https://logo.clearbit.com/{query}")
        # Use Pillow to open the image data and save it to a file
        image = Image.open(BytesIO(response.content))
        image.save("logo.png")
        return  # exit the function if Clearbit option succeeds
    except Exception as e:
        print("An error occurred trying to pull logo from clearbit:", e)
    
    try:
        # Get the HTML content of the website
        response = requests.get(f"https://{query}")
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the logo image using the src attribute
        logo_image = soup.find("img", {"src": re.compile(r'logo|cover', re.IGNORECASE)})
        if logo_image:
            # If logo image is found, download and save it
            logo_url = logo_image["src"]
            response = requests.get(logo_url)
            image = Image.open(BytesIO(response.content))
            image.save("logo.png")
        # Find the logo image using class name
        else:
            logo_image = soup.find("img", {"class": re.compile(r'logo|cover', re.IGNORECASE)})
            if logo_image:
                print("test")
                # If logo image is found, download and save it
                logo_url = logo_image["src"]
                response = requests.get(logo_url)
                image = Image.open(BytesIO(response.content))
                image.save("logo.png")
    except Exception as e:
        print("An error occurred trying to pull the logo from HTML:", e)