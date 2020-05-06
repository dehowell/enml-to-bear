
from .styles import *

def is_excerpt(element):
    # TODO need a function w/ heuristics to find excerpts in the doc
    pass

def convert_div_excerpt(tag):
    assert tag.name == 'div'
    tag.name = 'blockquote'

    # Replace all bold spans
    for span in tag.find_all('span', style=STYLE_EVERNOTE_BOLD):
        span.name = 'b'
        del span['style']

    # Replace all highlight spans with mark
    for span in tag.find_all('span', style=STYLE_EVERNOTE_HIGHLIGHT):
        span.name = 'mark'
        del span['style']

    return tag
