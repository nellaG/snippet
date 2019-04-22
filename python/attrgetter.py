from collections import namedtuple

metro_data = [
    ('Seoul', 'KR', 1.3, (4, 1)),
    ('Tokyo', 'JP', 1.2, (2, 3)),
    ('Mexico City', 'MX', 3.3, (2, 6)),
    ]

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

print(metro_areas[0])

assert metro_areas[0] == \
    Metropolis(name='Seoul', cc='KR', pop=1.3, coord=LatLong(lat=4, long=1))
