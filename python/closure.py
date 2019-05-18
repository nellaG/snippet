class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def main():
    print('class implementation')
    avg = Averager()
    assert avg(10) == 10.0
    assert avg(11) == 10.5
    assert avg(12) == 11.0

    print('high order function implementation')

    avg = make_averager()
    assert avg(10) == 10.0
    assert avg(11) == 10.5
    assert avg(12) == 11.0

    print('using nonlocal')

    avg = make_averager_nonlocal()
    assert avg(10) == 10.0
    assert avg(11) == 10.5
    assert avg(12) == 11.0


main()
