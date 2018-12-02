# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

from unicodedata import name, normalize


s1 = 'café'
s2 = 'cafe\u0301'  # U+0301 : CONBINING ACUTE ACCENT

assert len(s1) != len(s2)  # 4 != 5
assert s1 != s2
assert len(normalize('NFC', s1)) == len(normalize('NFC', s2)) == 4
assert len(normalize('NFD', s1)) == len(normalize('NFD', s2)) == 5
assert normalize('NFC', s1) == normalize('NFC', s2) == 'café'
assert normalize('NFD', s1) == normalize('NFD', s2) == 'cafe\u0301'

ohm = '\u2126'
ohm_c = normalize('NFC', ohm)

assert name(ohm) == 'OHM SIGN'
assert name(ohm_c) == 'GREEK CAPITAL LETTER OMEGA'
assert ohm != ohm_c
assert normalize('NFC', ohm) == normalize('NFC', ohm_c)

