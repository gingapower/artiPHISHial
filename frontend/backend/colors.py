import time
import re
from collections import Counter
import colorsys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

def extract_colors(url, css_content):
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    domain = urlparse(url).netloc
    color_patterns = {
        r"#([0-9a-fA-F]{6})": "hex",
        r"rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)": "rgb",
        r"rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\)": "rgba",
    }
    background_pattern = r"background(-color)?\s*:\s*(#([0-9a-fA-F]{6})|rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)|rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\));"
    font_pattern = r"font-family\s*:\s*(.*?);"
    color_counts = Counter()
    background_counts = Counter()
    font_counts = Counter()

    # Check for background color
    print(f"Searching for Background Colors in {domain}...")
    time.sleep(1)
    if "background" in css_content or "background-color" in css_content:
        background_matches = re.findall(background_pattern, css_content)
        if background_matches:
            background_counts.update(background_matches)
            for color, count in background_counts.most_common(2):
                background_color = color[1]
                print(f"Background color: {background_color}, Count: {count}")

    # Check for font family
    print(f"Searching for Font Family in {domain}...")
    time.sleep(1)
    if "font-family" in css_content:
        font_matches = re.findall(font_pattern, css_content)
        if font_matches:
            font_counts.update(font_matches)
            for font, count in font_counts.most_common(2):
                print(f"Font Family: {font}, Count: {count}")

    for pattern, color_type in color_patterns.items():
        matches = re.findall(pattern, css_content)
        if matches:
            print(f"{color_type} Color codes found in the CSS file:")
            time.sleep(2)

            # Convert RGBA colors to RGB
            if color_type == "rgba":
                matches = [(*map(int, match[:3]), float(match[3])) for match in matches]

            color_counts.update(matches)

            for color, count in color_counts.most_common(2):
                if color_type == "hex":
                    print(f"Color code: #{color}, Count: {count}")
                elif len(color) == 4:
                    print(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}")

            # Save colors in a txt file
            with open(f"colors/{domain}_{color_type}_colors.txt", "a") as f:
                for color, count in color_counts.most_common(2):
                    if color_type == "hex":
                        f.write(f"Color code: #{color}, Count: {count}\n")
                        print(f"Color code: #{color}, Count: {count}")
                    elif len(color) == 4:
                        f.write(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}\n")
                        print(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}")

        else:
            print(f"{color_type} not found")
        # Search for font-family in css
    font_family_pattern = r"font-family\s*:\s*([\w\s\',-]+)\s*;"
    font_family_matches = re.findall(font_family_pattern, css_content)
    if font_family_matches:
        print("Font Families found in the CSS file:")
        time.sleep(2)
        font_family_counts = Counter(font_family_matches)
        for font_family, count in font_family_counts.most_common(1):
            # Save font family in a txt file
            with open(f"fonts/{domain}_font_family.txt", "a") as f:
                f.write(f"Font Family: {font_family}, Count: {count}\n")
    else:
        print("Font Family not found")




