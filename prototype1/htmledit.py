import os
import re
import webbrowser
import configparser

def insert_css_links(webpage):
    config = configparser.ConfigParser()
    cwd = os.getcwd()
    folder_path = cwd+ "\\" + webpage
    css_files = [f for f in os.listdir(folder_path) if f.endswith(".css")]
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
        html_file_path = os.path.join(folder_path, "index.html")
        with open(html_file_path, "rb") as f:
            file_content = f.read().decode('utf-8', errors='ignore')
        file_content = file_content.replace('</head>', f'<link href="{css_filename}" rel="stylesheet" type="text/css" />\n</head>')
        with open(html_file_path, "w", encoding='utf-8') as f:
            f.write(file_content)
    
    url = f"file://{file_path}"
    print(url)
    webbrowser.open(url)
