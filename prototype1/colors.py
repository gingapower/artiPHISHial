import time
import re
from collections import Counter
import colorsys
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Read the HTML file
with open('login.html', 'r') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

def extract_colors(url, css_content):
    domain = urlparse(url).netloc
    color_patterns = {
        r"#([0-9a-fA-F]{6})": "hex",
        r"rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)": "rgb",
        r"rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\)": "rgba",
    }
    background_pattern = r"background(-color)?\s*:\s*(#([0-9a-fA-F]{6})|rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)|rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\));"
    color_counts = Counter()
    background_counts = Counter()
    #Check for background color
    print(f"Searching for Background Colors in {domain}...")
    time.sleep(1)
    if "background" in css_content or "background-color" in css_content:
        background_matches = re.findall(background_pattern, css_content)
        if background_matches:
            background_counts.update(background_matches)
            with open(f"colors/{domain}_background_colors.txt", "a") as f:
                for color, count in background_counts.most_common(2):
                    background_color = color[1]
                    f.write(f"Background color: {background_color}, Count: {count}\n")
                    print(f"Background color: {background_color}, Count: {count}")


    for pattern, color_type in color_patterns.items():
        matches = re.findall(pattern, css_content)
        if matches:
            print(f"{color_type} Color codes found in the CSS file:")
            time.sleep(2)

            # Convert RGBA colors to RGB
            if color_type == "rgba":
                matches = [(*map(int, match[:3]), float(match[3])) for match in matches]

            color_counts.update(matches)

            # Save colors in a txt file
            with open(f"colors/{domain}_{color_type}_colors.txt", "a") as f:
                for color, count in color_counts.most_common(2):
                    if color_type == "hex":
                        f.write(f"Color code: #{color}, Count: {count}\n")
                        print(f"Color code: #{color}, Count: {count}")
                    elif len(color) == 4:
                        f.write(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}\n")
                        print(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}")

            # Get the second most common color
            if color_type == "hex":
                color = color_counts.most_common(1)[0][0]
                login_button = soup.find('button', {'id': 'login-button'})
                # Set the login button's background-color to the second color
                login_button['style'] = f'background-color: #{color};'

                # Write the modified HTML back to the file
                with open('login.html', 'w') as f:
                    f.write(str(soup))

        else:
            print(f"{color_type} not found")
