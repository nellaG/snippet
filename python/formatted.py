'''formatted'''


def brl_to_usd():
    """ brl_to_usd """
    brl = 1/2.43
    assert format(brl, '0.4f') == '0.4115'
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))


if __name__ == '__main__':
    brl_to_usd()

    assert format(42, 'b') == '101010'
    assert format(2/3, '.1%') == '66.7%'
