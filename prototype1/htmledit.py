import os
import re
import webbrowser
import configparser

def insert_css_links(webpage):
    config = configparser.ConfigParser()
    cwd = os.getcwd()
    folder_path = cwd+ "\\" + webpage
    css_files = []
    all_files = os.listdir(folder_path)

# loop through each file and add .css if it doesn't have an extension

    for file_name in all_files:
        if '.' in file_name:
            css_files.append(file_name)
        else:
            css_file_name = file_name + '.css'
            css_files.append(css_file_name)
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, css_file_name))

# print the list of CSS files
    print(css_files)

    
    # Get the current working directory
    cwd = os.getcwd()
    #Read the config file
    config.read('config.ini')
    # Get the browser path
    browser_path = config.get('browser', 'path')
    os.environ['BROWSER'] = browser_path
    # Define the relative path to the file
    relative_path = webpage + "\\index.html"
    # Combine the current working directory and the relative path
    file_path = os.path.join(cwd, relative_path)

    for css_file in css_files:
        css_filename = os.path.basename(css_file)
        css_path = "{""{"" url_for('static', filename='"+css_filename+"') ""}""}"
        html_file_path = os.path.join(folder_path, "index.html")
        with open(html_file_path, "rb") as f:
            file_content = f.read().decode('utf-8', errors='ignore')
        file_content = file_content.replace('</head>', f'<link href="{css_path}" rel="stylesheet" type="text/css" />\n</head>')
        with open(html_file_path, "w", encoding='utf-8') as f:
            f.write(file_content)
    
    url = f"file://{file_path}"
    print(url)
    webbrowser.open(url)

#insert_css_links("www.linkedin.com")