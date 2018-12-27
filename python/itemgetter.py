from operator import itemgetter

metro_data = [
    ('Seoul', 'KR', 1.3, (4, 1)),
    ('Tokyo', 'JP', 1.2, (2, 3)),
    ('Mexico City', 'MX', 3.3, (2, 6)),
    ]

out = []
for city in sorted(metro_data, key=itemgetter(1)):
    out.append(city)

print(out)
assert out == [
        ('Tokyo', 'JP', 1.2, (2, 3)),
        ('Seoul', 'KR', 1.3, (4, 1)),
        ('Mexico City', 'MX', 3.3, (2, 6))
]

cc_name = itemgetter(1, 0)

out = []
for city in metro_data:
    out.append(cc_name(city))

print(out)
assert out == [('KR', 'Seoul'), ('JP', 'Tokyo'), ('MX', 'Mexico City')]

