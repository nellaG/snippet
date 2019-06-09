from array import array
import math

class Vector2d:

    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, octets):
        """ frombytes """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)


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

    assert v1.__dict__ == {'_Vector2d__y': 4.0, '_Vector2d__x': 3.0}
    assert v1._Vector2d__x == 3.0
