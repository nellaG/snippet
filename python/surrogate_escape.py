# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

import os


piname = 'digits-of-π'
piname_bytes = b'digits-of-\xcf\x80'

filename = 'digits-of-pi'

piname_str = piname_bytes.decode('ascii', 'surrogateescape')
'''
Low Surrogate Area: no characters or names are provided for this range.
Range: U+DC00-U+DCFF

e.g. \xcf -> \udccf
'''
assert piname_str == 'digits-of-\udccf\udc80'

assert piname_str.encode('ascii', 'surrogateescape') == piname_bytes
