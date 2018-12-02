# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab
import array

numbers = array.array('h', [-2, 1, 0, 1, 2])
octets = bytes(numbers)

# b'\xfe\xff\x01\x00\x00\x00\x01\x00\x02\x00'
print(octets)
