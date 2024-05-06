from bs4 import BeautifulSoup
import cssutils

def parse_css(css_file):
    css = cssutils.parseFile(css_file)
    rules = css.cssRules
    css_dict = {}

    for rule in rules:
        if rule.type == rule.STYLE_RULE:
            selectors = rule.selectorText.split(',')
            for selector in selectors:
                selector = selector.strip()
                if selector not in css_dict:
                    css_dict[selector] = []
                css_dict[selector].append(rule.style)

    return css_dict

def parse_html(html_file, css_dict):
    with open(html_file, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(True)

    result = {}

    for element in elements:
        for css_selector, css_styles in css_dict.items():
            if element.name in css_selector or \
                (css_selector.startswith('.') and css_selector[1:] in element.get('class', [])) or \
                (css_selector.startswith('#') and css_selector[1:] == element.get('id', '')):
                if css_selector not in result:
                    result[css_selector] = []
                result[css_selector].append([element.name, element.sourceline])

    return result

def main():
    css_file_path = input("Введіть шлях до CSS файлу: ")
    html_file_path = input("Введіть шлях до HTML файлу: ")

    css_dict = parse_css(css_file_path)
    result = parse_html(html_file_path, css_dict)
    
    # Конвертуємо результат у потрібний формат
    formatted_result = {}
    for selector, elements in result.items():
        formatted_result[selector] = []
        for element in elements:
            tag, line = element
            formatted_result[selector].append([tag, line])

    print(formatted_result)

if __name__ == "__main__":
    main()
