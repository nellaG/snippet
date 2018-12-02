# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

name = 'São Paulo'

print(name.encode('utf_8'))
print(name.encode('utf_16'))
print(name.encode('iso8859_1'))  # latin1

try:
    print(name.encode('cp437'))  # the character set of the original IBM PC
except UnicodeEncodeError:
    print('cp437: UnicodeEncodeError')


# ignore: skip the character (bad practice)
print(name.encode('cp437', errors='ignore'))  # So Paulo


# replace: show the character as '?' (causes the loss of data but noticeable)
print(name.encode('cp437', errors='replace'))  # S?o Paulo


# xmlcharrefreplace: change the character to XML object
print(name.encode('cp437', errors='xmlcharrefreplace'))  # S&#227;o Paulo


octets = b'Montr\xe9al'

# cp1252: Windows 1252. Superset of latin1
print(octets.decode('cp1252'))  # Montréal

# iso8859-7: for the greek alphabet
print(octets.decode('iso8859_7'))  # Montrιal

# koi8_r: for the cyrillic alphabet
print(octets.decode('koi8_r'))  # MontrИal

try:
  octets.decode('utf-8')
except UnicodeDecodeError as e:
  print(e)

# changes \xe9 to � (U+FFFD)
# which is the official replacement character of unicode
print(octets.decode('utf-8', errors='replace'))
