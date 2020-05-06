
from .styles import *

def is_excerpt(element):
    # TODO need a function w/ heuristics to find excerpts in the doc
    pass

def convert_div_excerpt(tag):
    assert tag.name == 'div'
    tag.name = 'blockquote'

    # Replace all bold spans with <bold>
    for span in tag.find_all('span', style=STYLE_EVERNOTE_BOLD):
        span.name = 'b'
        del span['style']
    
    return tag
