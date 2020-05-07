
from bs4 import BeautifulSoup

from .styles import *

# BeautifulSoup object for generating new tags.
SOUP = BeautifulSoup(features='html.parser')

def has_highlight(styles):
    return (styles is not None
        and STYLE_EVERNOTE_HIGHLIGHT in styles
        and STYLE_EVERNOTE_HIGHLIGHT_BG in styles)

def has_bold(styles):
    return (styles is not None
        and STYLE_EVERNOTE_BOLD in styles)

def is_excerpt(element):
    # TODO need a function w/ heuristics to find excerpts in the doc
    return (element.name == 'div'
        and element.string is not None
        and not element.string.startswith('PAGE'))

def convert_div_excerpt(tag):
    assert tag.name == 'div'
    tag.name = 'blockquote'

    # Replace all highlight + bold spans with b and mark
    for span in tag.find_all('span', style=lambda s: has_bold(s) and has_highlight(s)):
        span.name = 'mark'
        span.wrap(SOUP.new_tag('b'))
        del span['style']

    # Replace all highlighted b with mark
    for span in tag.find_all('b', style=has_highlight):
        span.name = 'mark'
        span.wrap(SOUP.new_tag('b'))
        del span['style']

    # Replace all bold spans with b
    for span in tag.find_all('span', style=has_bold):
        span.name = 'b'
        del span['style']

    # Replace all highlight spans with mark
    for span in tag.find_all('span', style=has_highlight):
        span.name = 'mark'
        del span['style']

    return tag


def convert(enml):
    soup = BeautifulSoup(enml, features="html.parser")

    for div in soup.find_all('div'):
        if is_excerpt(div):
            print(div)
            # convert_div_excerpt(div)

    soup.find('en-note').unwrap()
    return str(soup)