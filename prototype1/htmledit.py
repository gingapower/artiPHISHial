import os
import webbrowser
import configparser

def insert_css_links(webpage):
    config = configparser.ConfigParser()
    cwd = os.getcwd()
    folder_path = cwd+ "\\" + "websites\\" + webpage
    html_file_path = folder_path + "\\index.html"
    css_files = []
    all_files = os.listdir(folder_path)

    for file_name in all_files:
        if '.' in file_name:
            css_files.append(file_name)
        else:
            css_file_name = file_name + '.css'
            css_files.append(css_file_name)
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, css_file_name))

    for css_file in css_files:
        css_filename = os.path.basename(css_file)
        css_path = "{""{"" url_for('static', filename='"+css_filename+"') ""}""}"
        with open(html_file_path, "rb") as f:
            file_content = f.read().decode('utf-8', errors='ignore')
        file_content = file_content.replace('</head>', f'<link href="{css_path}" rel="stylesheet" type="text/css" />\n</head>')
        with open(html_file_path, "w", encoding='utf-8') as f:
            f.write(file_content)

    #Open in Webbrowser
    config.read('config.ini')
    browser_path = config.get('browser', 'path')
    os.environ['BROWSER'] = browser_path
    url = f"file://{html_file_path}"
    webbrowser.open(url)

