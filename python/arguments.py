''' arguments '''


def tag(name, cls=None, *content, **attrs):
    ''' creates tags '''
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name)
                         for c in content)
    return '<%s%s />' % (name, attr_str)


def tagcall():
    ''' call '''
    assert tag('br') == '<br />'
    assert tag('p', None, 'hello') == '<p>hello</p>'
    assert tag('p', None, 'hello', 'world') == '<p>hello</p>\n<p>world</p>'
    assert tag('p', None, 'hello', id=33) == '<p id="33">hello</p>'
    assert tag('p', 'sidebar', 'hello', 'world') == \
        '<p class="sidebar">hello</p>\n<p class="sidebar">world</p>'
    _tag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'cls': 'framed'
    }
    assert tag(**_tag) == \
        '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'


def func(a, * , b):
    return a, b


def funccall():
    assert func(1, b=2) == (1, 2)


def main():
    print('tag calling...')
    tagcall()
    print('func calling...')
    funccall()


main()
