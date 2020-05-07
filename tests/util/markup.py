from functools import partial
import textwrap

from enml_to_bear import SOUP
from enml_to_bear.styles import *


def wrap(text):
    return ' '.join(textwrap.wrap(textwrap.dedent(text)))


def make_element(*elements, tag='div', styles=None):
    tag = SOUP.new_tag(tag)
    if styles is not None:
        if type(styles) == str:
            tag['style'] = styles
        else:
            tag['style'] = ';'.join(styles)
    for element in elements:
        tag.append(element)
    return tag

# DSL functions for common tags
div = partial(make_element, tag='div')
b = partial(make_element, tag='b')
span = partial(make_element, tag='span')
mark = partial(make_element, tag='mark')
quote = partial(make_element, tag='blockquote')
