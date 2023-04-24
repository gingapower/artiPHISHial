from bs4 import BeautifulSoup
import chardet

# Replace 'example.html' with the path to your HTML file
with open('index.html', 'rb') as f:
    data = f.read()
    encoding = chardet.detect(data)['encoding']
    html = data.decode(encoding)

soup = BeautifulSoup(html, 'html.parser')

forms = soup.find_all('form')

for form in forms:
    inputs = form.find_all('input')
    if inputs:
        print(f'Found {len(inputs)} input fields in form:')
        print(inputs)
    else:
        print('No input fields found in form:')
        #print(form)
