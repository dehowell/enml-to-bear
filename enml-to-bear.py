import sys

from bs4 import BeautifulSoup

if __name__ == '__main__':

    enex_file = sys.argv[1]

    with open(enex_file) as f:
        enex = f.read()
        soup = BeautifulSoup(enex, features="html.parser")
        enml = soup.find('content').string

    polar = enml_to_polar(enml)
    print(polar)