import copy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)  # don't use passengers itself

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)  # shallow copy

    bus3 = copy.deepcopy(bus1)  # deep copy
    bus1.drop('Bill')
    assert bus2.passengers == ['Alice', 'Claire', 'David']
    assert bus1.passengers == bus2.passengers
    assert bus3.passengers == ['Alice', 'Bill', 'Claire', 'David']
