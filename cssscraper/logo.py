import requests
import shutil
from googlesearch import search

def extract_logo(query):
    url = ""

    for j in search(query, num=1, stop=1):
        url = j

    if url != "":
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open("spotify_logo.png", 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print("Logo downloaded successfully.")
    else:
        print("No images found.")



        # page = requests.get(url)
        # soup = BeautifulSoup(page.content, "html.parser")
        # logo_link = None
        # for img in soup.find_all("img"):
        #     if ("logo" or "title" or "image" or "Logo" or "cover" or "Cover" or "Title") in img.get("src"):
        #         logo_link = img.get("src")
        #         break
        # return logo_link



