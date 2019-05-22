import weakref


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

assert sorted(stock.keys()) == ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

del catalog

assert sorted(stock.keys()) == ['Parmesan']

del cheese

assert sorted(stock.keys()) == []
