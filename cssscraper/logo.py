import requests
from bs4 import BeautifulSoup


def extract_logo(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    logo_link = None
    for img in soup.find_all("img"):
        if ("logo" or "title" or "image" or "Logo" or "cover" or "Cover" or "Title") in img.get("src"):
            logo_link = img.get("src")
            break
    return logo_link
