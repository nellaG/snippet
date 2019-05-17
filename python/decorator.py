def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco  # executes at import time
def target():
    print('running target()')


target()  # running inner()
assert target.__repr__().startswith('<function deco.<locals>.inner at')


promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    print(distinct_items)
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)
