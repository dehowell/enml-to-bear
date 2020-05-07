import sys

from bs4 import BeautifulSoup

import enml_to_bear

if __name__ == '__main__':
    enex_file = sys.argv[1]

    with open(enex_file) as f:
        enex = f.read()
        soup = BeautifulSoup(enex, features="html.parser")
        enml = soup.find('content').string

    html = enml_to_bear.convert(enml)
    print(html)