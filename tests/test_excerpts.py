import textwrap
import unittest

from bs4 import BeautifulSoup

import enml_to_bear
from enml_to_bear.styles import *

def wrap(text):
    return ' '.join(textwrap.wrap(textwrap.dedent(text)))


def make_element(*elements, tag='div'):
    tag = BeautifulSoup(features='html.parser').new_tag(tag)
    for element in elements:
        tag.append(element)
    return tag

def div(*elements):
    return make_element(*elements, tag='div')

def quote(*elements):
    return make_element(*elements, tag='blockquote')

def evernote_bold(*elements):
    span = make_element(*elements, tag='span')
    span['style'] = STYLE_EVERNOTE_BOLD
    return span

def evernote_highlight(*elements):
    span = make_element(*elements, tag='span')
    span['style'] = STYLE_EVERNOTE_HIGHLIGHT
    return span

def evernote_highlighted_bold(*elements):
    span = make_element(*elements, tag='span')
    span['style'] = STYLE_EVERNOTE_BOLD_AND_HIGHLIGHT
    return span

def bold(*elements):
    return make_element(*elements, tag='b')

def mark(*elements):
    return make_element(*elements, tag='mark')

class TestExcerpts(unittest.TestCase):

    def test_quote_unstyled_excerpt(self):
        text = "Lorem ipsum dolor sit amet"
        excerpt = div(text)
        converted = enml_to_bear.convert_div_excerpt(excerpt)
        self.assertEquals(converted, quote(text))

    def test_convert_bold(self):
        excerpt = div("Lorem ipsum ", evernote_bold("dolor sit amet"))
        converted = enml_to_bear.convert_div_excerpt(excerpt)
        self.assertEquals(converted,
            quote("Lorem ipsum ", bold("dolor sit amet")))

    def test_convert_highlight(self):
        excerpt = div("Lorem ipsum ", evernote_highlight("dolor sit amet"))
        converted = enml_to_bear.convert_div_excerpt(excerpt)
        self.assertEquals(converted,
            quote("Lorem ipsum ", mark("dolor sit amet")))
