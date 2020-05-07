from itertools import permutations
import unittest

from util.markup import *
from enml_to_bear import convert_div_excerpt

# ===== EVERNOTE REPRESENTATIONS IN HTML
# PLAIN PHRASE
# <div>Lorem ipsum dolor sit amet</div>
#
# BOLD PHRASE
# <div>Lorem ipsum <b>dolor sit amet</b></div>
#
# LEGACY BOLD PHRASE
# <div>Lorem ipsum <span style="font-weight: bold;">dolor sit amet</span></div>
#
# HIGHLIGHTED PHRASE
# <div>Lorem ipsum <span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></div>
#
# HIGHLIGHTED AND BOLDED PHRASE
# <div>Lorem ipsum <b style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</b></div>
#
# LEGACY HIGHLIGHTED AND BOLDED PHRASE
# <div>Lorem ipsum <span style="font-weight: bold; background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></div>
#
# HIGHLIGHT IN BOLD PHRASE
# <div><b>Lorem ipsum <span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></b></div>
#
# LEGACY HIGHLIGHT IN BOLD PHRASE
# <div><span style="font-weight: bold;">Lorem ipsum </span><span style="background-color: rgb(255, 250, 165); font-weight: bold;-evernote-highlight:true;">dolor sit amet</span></div>

# ===== BEAR REPRESENTATIONS IN HTML
# PLAIN PHRASE
# <p>Lorem ipsum dolor sit amet</p>
#
# BOLD PHRASE
# <p>Lorem ipsum <b>dolor sit amet</b></p>
#
# HIGHLIGHTED PHRASE
# <p>Lorem ipsum <mark>dolor sit amet</mark></p>
#
# HIGHLIGHTED AND BOLDED PHRASE
# <p>Lorem ipsum <b><mark>dolor sit amet</mark></b></p>
#
# HIGHLIGHT IN BOLD PHRASE
# <p><b>Lorem ipsum <mark>dolor sit amet</mark></b></p>

class TestMarkupConversions(unittest.TestCase):

    def test_convert_plain_phrase(self):
        actual = convert_div_excerpt(div("Lorem ipsum dolor sit amet"))
        expected = p("Lorem ipsum dolor sit amet")
        self.assertEqual(actual, expected)

    def test_convert_legacy_bold_phrase(self):
        enml = div("Lorem ipsum ", span("dolor sit amet", styles=STYLE_EVERNOTE_BOLD))
        actual = convert_div_excerpt(enml)
        expected = p("Lorem ipsum ", b("dolor sit amet"))
        self.assertEqual(actual, expected)

    def test_convert_bold_phrase(self):
        enml = div("Lorem ipsum ", b("dolor sit amet"))
        actual = convert_div_excerpt(enml)
        expected = p("Lorem ipsum ", b("dolor sit amet"))
        self.assertEqual(actual, expected)

    def test_convert_highlighted_phrase(self):
        attributes = [STYLE_EVERNOTE_HIGHLIGHT_BG, STYLE_EVERNOTE_HIGHLIGHT]
        for styles in permutations(attributes, len(attributes)):
            enml = div("Lorem ipsum ", span("dolor sit amet", styles=styles))
            actual = convert_div_excerpt(enml)
            expected = p("Lorem ipsum ", mark("dolor sit amet"))
            self.assertEqual(actual, expected, 'Failed with styles {}'.format(styles))

    def test_convert_legacy_highlighted_and_bolded_phrase(self):
        attributes = [STYLE_EVERNOTE_BOLD, STYLE_EVERNOTE_HIGHLIGHT_BG, STYLE_EVERNOTE_HIGHLIGHT]
        for styles in permutations(attributes, len(attributes)):
            enml = div("Lorem ipsum ", span("dolor sit amet", styles=styles))
            actual = convert_div_excerpt(enml)
            expected = p("Lorem ipsum ", b(mark("dolor sit amet")))
            self.assertEqual(actual, expected, 'Failed with styles {}'.format(styles))

    def test_convert_highlighted_and_bolded_phrase(self):
        attributes = [STYLE_EVERNOTE_HIGHLIGHT_BG, STYLE_EVERNOTE_HIGHLIGHT]
        for styles in permutations(attributes, len(attributes)):
            enml = div("Lorem ipsum ", b("dolor sit amet", styles=styles))
            actual = convert_div_excerpt(enml)
            expected = p("Lorem ipsum ", b(mark("dolor sit amet")))
            self.assertEqual(actual, expected, 'Failed with styles {}'.format(styles))

    @unittest.skip("merged bold spans not yet implemented")
    def test_convert_legacy_highlight_in_bold_phrase(self):
        attributes = [STYLE_EVERNOTE_BOLD, STYLE_EVERNOTE_HIGHLIGHT_BG, STYLE_EVERNOTE_HIGHLIGHT]
        for hl_styles in permutations(attributes, len(attributes)):
            enml = div(
                span("Lorem ipsum ", styles=STYLE_EVERNOTE_BOLD),
                span("dolor sit amet", styles=hl_styles)
            )
            actual = convert_div_excerpt(enml)
            expected = p(b("Lorem ipsum ", mark("dolor sit amet")))
            self.assertEqual(actual, expected, 'Failed with styles {}'.format(hl_styles))

    def test_convert_highlight_in_bold_phrase(self):
        attributes = [STYLE_EVERNOTE_HIGHLIGHT_BG, STYLE_EVERNOTE_HIGHLIGHT]
        for hl_styles in permutations(attributes, len(attributes)):
            enml = div(b("Lorem ipsum ", span("dolor sit amet", styles=hl_styles)))
            actual = convert_div_excerpt(enml)
            expected = p(b("Lorem ipsum ", mark("dolor sit amet")))
            self.assertEqual(actual, expected, 'Failed with styles {}'.format(hl_styles))