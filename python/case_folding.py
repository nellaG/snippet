# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

from unicodedata import name

micro = 'µ'
eszett = 'ß'

assert name(micro) == 'MICRO SIGN'
micro_cf = micro.casefold()
assert name(micro_cf) == 'GREEK SMALL LETTER MU'

assert name(eszett) == 'LATIN SMALL LETTER SHARP S'
eszett_cf = eszett.casefold()

assert eszett_cf == 'ss'
