
from bs4 import BeautifulSoup

from .styles import *

# BeautifulSoup object for generating new tags.
SOUP = BeautifulSoup(features='html.parser')

def is_excerpt(element):
    # TODO need a function w/ heuristics to find excerpts in the doc
    pass

def convert_div_excerpt(tag):
    assert tag.name == 'div'
    tag.name = 'blockquote'

    # Replace all bold spans with b
    for span in tag.find_all('span', style=STYLE_EVERNOTE_BOLD):
        span.name = 'b'
        del span['style']

    # Replace all highlight spans with mark
    for span in tag.find_all('span', style=STYLE_EVERNOTE_HIGHLIGHT):
        span.name = 'mark'
        del span['style']


    # Replace all highlight and bold spans with b and mark
    for span in tag.find_all('span', style=STYLE_EVERNOTE_BOLD_AND_HIGHLIGHT):
        span.name = 'mark'
        span.wrap(SOUP.new_tag('b'))
        del span['style']

    return tag
