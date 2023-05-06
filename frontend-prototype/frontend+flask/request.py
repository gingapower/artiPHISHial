import requests
import json
import configparser
import os
import webbrowser

def generatepage(domain):
    name = input("Enter name of the company: ")
    url = "https://api.openai.com/v1/chat/completions"
    config = configparser.ConfigParser()

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "please generate me html code of a loginpage for a company named"+name+". stylesheet=style.css and also an image: logo.png which should be in a mini size"}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()

    # Remove newline characters and tab characters
    response_content = response_data['choices'][0]['message']['content']
    response_content = response_content.replace('\n', '').replace('\t', '')
    with open('index.html', 'w') as file:
        file.write(response_content)
    html = response_content

    # Assign the two most common colors to color1 and color2
    with open(f"colors/{domain}_hex_colors.txt", "r") as f:
        lines = f.readlines()
        color1 = lines[0].split()[2][1:]
        color2 = lines[1].split()[2][1:]

    # Get the font family from the font_family.txt file
    with open(f"fonts/{domain}_font_family.txt", "r") as f:
        font_style = f.read().strip()

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "create me a advancded css file for html:"+html+". The colors should  be "+color1+" and "+color2+" and in a modern and professional style with "+font_style+" as font family style. Simple animations at the button."}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()

    # Remove newline characters and tab characters
    response_content = response_data['choices'][0]['message']['content']
    response_content = response_content.replace('\n', '').replace('\t', '')
    with open('style.css', 'w') as file:
        file.write(response_content)

    config.read('config.ini')
    # Get the browser path
    browser_path = config.get('browser', 'path')
    os.environ['BROWSER'] = browser_path
    # Open the generated HTML file in the default browser
    webbrowser.open('index.html')
