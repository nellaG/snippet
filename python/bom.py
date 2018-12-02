# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab


u16 = 'El Niño'.encode('utf_16')

# \xff\xfe : BOM (byte order mark)
print(u16)  # b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'

# E : U+0045 (69) -> [69, 0] (little endian)
print(list(u16)) # [255, 254, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]

# U+FEFF (ZERO WIDTH NO-BREAK SPACE) is encoded to b'\xff\xfe in little endian
# utf_16le and utf_16be doesn't generate BOM character.
u16le = 'El Niño'.encode('utf_16le')
print(list(u16le))  # [69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]

u16be = 'El Niño'.encode('utf_16be')
print(list(u16be))  # [0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]
