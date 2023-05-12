import requests
import json
import configparser
import os
import webbrowser

def generatepage(domain):
    name = input("Enter name of the company: ")
    
    # Load API key from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config.get('api', 'key')
    
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    model = "gpt-3.5-turbo-0301"

    # Generate HTML code
    html_prompt = f"please generate me html code of a loginpage for a company named {name}. stylesheet=style.css and also an image: logo.png which should be in a mini size"
    html_response = generate_response(model, headers, html_prompt)
    html = cleanup_response(html_response)

    # Generate CSS code
    color1, color2 = get_hex_colors(domain)
    font_style = get_font_family(domain)
    css_prompt = f"create me a advancded css file for html:{html}. The colors should be {color1} and {color2} and in a modern and professional style with {font_style} as font family style. Simple animations at the button."
    css_response = generate_response(model, headers, css_prompt)
    css = cleanup_response(css_response)

    # Save HTML and CSS files
    with open('index.html', 'w') as file:
        file.write(html)
    with open('style.css', 'w') as file:
        file.write(css)

    # Open the generated HTML file in the default browser
    open_in_browser('index.html')

def generate_response(model, headers, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    print(response_data)
    return response_data['choices'][0]['message']['content']

def cleanup_response(response_content):
    return response_content.replace('\n', '').replace('\t', '')

def get_hex_colors(domain):
    with open(f"colors/{domain}_hex_colors.txt", "r") as f:
        lines = f.readlines()
        color1 = lines[0].split()[2][1:]
        color2 = lines[1].split()[2][1:]
        return color1, color2

def get_font_family(domain):
    with open(f"fonts/{domain}_font_family.txt", "r") as f:
        return f.read().strip()

def open_in_browser(filename):
    config = configparser.ConfigParser()
    config.read('config.ini')
    browser_path = config.get('browser', 'path')
    os.environ['BROWSER'] = browser_path
    webbrowser.open(filename)
