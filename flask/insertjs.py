from calendar import c
from bs4 import BeautifulSoup
import os
import chardet
import re


# Read the HTML file
with open('index.html', 'rb') as f:
    data = f.read()
    encoding = chardet.detect(data)['encoding']
    html = data.decode(encoding)

# Remove all the form tags from the HTML
html = re.sub(r"<form.*?>", "", html)
html = re.sub(r"</form>", "", html)

# Insert the form tag before the body tag
soup = BeautifulSoup(html, 'html.parser')
body = soup.body
form = soup.new_tag('form', attrs={'method': 'post'})
#form.attrs = {'method': form.attrs['method'], 'action': form.attrs['action']}
body.insert_before(form)
form.append(body)



# Write the modified HTML back to the index.html file
with open("index.html", "w") as f:
    f.write(str(soup))

# Read the contents of the file
with open('index.html', 'r') as f:
    file_contents = f.read()

# Use regex to find the form element and modify its attributes
new_contents = re.sub(r'<form method="post">', '<form method="post" action="/submit_data">', file_contents)

# Write the modified contents back to the file
with open('index.html', 'w') as f:
    f.write(new_contents)

