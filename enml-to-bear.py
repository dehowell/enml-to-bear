import sys

from bs4 import BeautifulSoup

def enml_to_polar(text):
    soup = BeautifulSoup(text, features="html.parser")
    soup = BeautifulSoup(soup.find('content').string, features="html.parser")

    # Replace all highlight spans with <highlight>
    for span in soup.find_all('span', style='background-color: rgb(255, 250, 165); font-weight: bold;-evernote-highlight:true;'):
        span.name = 'b'
        del span['style']
        span.string.wrap(soup.new_tag('mark'))

    # Replace all bold spans with <bold>
    for span in soup.find_all('span', style="font-weight: bold;"):
        span.name = 'b'
        del span['style']
    
    soup.find('en-note').unwrap()
    return str(soup)

if __name__ == '__main__':

    enex_file = sys.argv[1]

    with open(enex_file) as f:
        enex = f.read()
        soup = BeautifulSoup(enex, features="html.parser")
        enml = soup.find('content').string

    polar = enml_to_polar(enml)
    print(polar)