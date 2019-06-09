from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        """ frombytes """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    print('--------')
    v1 = Vector2d(3, 4)
    assert v1.x == 3.0 and v1.y == 4.0
    x, y = v1
    assert x == 3.0 and y == 4.0
    v1_clone = eval(repr(v1))
    assert v1 == v1_clone

    octets = bytes(v1)
    assert abs(v1) == 5.0
    assert bool(v1) is True and bool(Vector2d(0, 0)) is False
