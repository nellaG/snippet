''' single dispatch '''

from collections import abc
from functools import singledispatch
import html
import numbers


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def __(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def ___(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
