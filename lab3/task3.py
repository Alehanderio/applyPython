from bs4 import BeautifulSoup
import re

def extract_css_styles(css_file_path):
    with open(css_file_path, 'r') as file:
        css_content = file.read()

    css_styles = {}
    matches = re.finditer(r'([^\{\}]+)\s*\{', css_content)
    for match in matches:
        selector_name = match.group(1).strip()
        line_number = css_content.count('\n', 0, match.start()) + 1
        css_styles.setdefault(selector_name, []).append(line_number)

    return css_styles

def extract_html_tags(html_file_path):
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    tags = re.findall(r'<([a-zA-Z0-9]+)[\s>]', html_content)
    return tags

def main(html_file_path, css_file_path):
    css_styles = extract_css_styles(css_file_path)
    html_tags = extract_html_tags(html_file_path)

    tag_styles = {}
    for selector, line_numbers in css_styles.items():
        for tag in html_tags:
            if tag in selector:
                tag_styles.setdefault(tag, []).extend(line_numbers)

    return tag_styles

if __name__ == "__main__":
    html_file_path = input("Enter the path to the HTML file: ")
    css_file_path = input("Enter the path to the CSS file: ")
    styles_dict = main(html_file_path, css_file_path)
    print(styles_dict)
