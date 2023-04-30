import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "please generate me just html code of a loginpage for a company named paypal. stylesheet=style.css and also an image: logo.png which should be a small size"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_data = response.json()

# Remove newline characters and tab characters
response_content = response_data['choices'][0]['message']['content']
response_content = response_content.replace('\n', '').replace('\t', '')
with open('index.html', 'w') as file:
    file.write(response_content)
print(response_content)
html = response_content

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

color1="#ffffff"
color2="#000000"

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "create me a css file. colors should  be"+color1+" and "+color2+" and in a modern style. simple animations at the button. html:"+html}]
}
response = requests.post(url, headers=headers, data=json.dumps(data))
response_data = response.json()

# Remove newline characters and tab characters
response_content = response_data['choices'][0]['message']['content']
response_content = response_content.replace('\n', '').replace('\t', '')
print(response_content)
with open('style.css', 'w') as file:
    file.write(response_content)
print(response_content)