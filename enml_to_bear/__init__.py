

def is_excerpt(element):
    # TODO need a function w/ heuristics to find excerpts in the doc
    pass

def convert_div_excerpt(tag):
    assert tag.name == 'div'
    tag.name = 'blockquote'
    return tag
