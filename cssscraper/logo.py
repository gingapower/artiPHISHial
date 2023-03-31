import requests
from PIL import Image
from io import BytesIO

def extract_logo(query):
    #Call clearbit API to get the logo image
    response = requests.get(f"https://logo.clearbit.com/{query}")
    # Use Pillow to open the image data and save it to a file
    image = Image.open(BytesIO(response.content))
    image.save(f"logo{query}.png")



