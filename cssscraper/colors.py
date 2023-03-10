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

    color_counts = Counter()

    for pattern, color_type in color_patterns.items():
        matches = re.findall(pattern, css_content)
        if matches:
            print(f"{color_type} Color codes found in the CSS file:")
            time.sleep(2)

            # Convert RGBA colors to RGB
            if color_type == "rgba":
                matches = [(*map(int, match[:3]), float(match[3])) for match in matches]

            # Convert RGB/RGBA colors to HSL
            if color_type in ["rgb", "rgba"]:
                matches = [colorsys.rgb_to_hls(*map(lambda x: x / 255, match[:3])) + (match[3],) for match in matches]

            color_counts.update(matches)

            print("Most common colors:")
            for color, count in color_counts.most_common(5):
                if color_type == "hex":
                    print(f"Color code: #{color}, Frequency: {count}")
                else:
                    print(f"Color code: {color_type}({', '.join(map(str, color))}), Frequency: {count}")
                print("")

            print("-----Done-----")
        else:
            print(f"{color_type} not found")


__all__ = ["extract_colors"]
