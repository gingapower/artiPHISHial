import time
import re
from collections import Counter
import colorsys


def extract_colors(css_content):
    color_patterns = {
        r"#([0-9a-fA-F]{6})": "hex",
        r"rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)": "rgb",
        r"rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\)": "rgba",
    }

    background_pattern = r"background(-color)?\s*:\s*(#([0-9a-fA-F]{6})|rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)|rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*((\d*(\.\d+)?)|1\.0+)\));"
    color_counts = Counter()
    background_counts = Counter()
    #Check for background color
    print("Searching for Background Colors ...")
    time.sleep(1)
    if "background" in css_content or "background-color" in css_content:
        background_matches = re.findall(background_pattern, css_content)
        if background_matches:
            background_counts.update(background_matches)
            for color, count in background_counts.most_common(5):
                background_color = color[1]
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


                      
            print("Most common colors:")
            for color, count in color_counts.most_common(5):
                if color_type == "hex":
                    print(f"Color code: #{color}, Count: {count}")
                elif len(color) == 4:
                    print(f"Color code: {color_type}({', '.join(map(str, color))}), Count: {count}")
                print("")

            print("-----Done-----")
        else:
            print(f"{color_type} not found")

__all__ = ["extract_colors"]
