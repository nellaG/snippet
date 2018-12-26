# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

import pyuca


coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

sorted_fruits = sorted(fruits, key=coll.sort_key)
assert sorted_fruits == ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
