''' simple decorator '''
import functools
import time


def clock(func):
    '''clock'''
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        '''clocked'''
        t0 = time.time()  # noqa
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


# with no lru_cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 2) + fibonacci_lru(n - 1)


if __name__ == '__main__':
    snooze(.123)
    print('=====================')
    print(fibonacci(6))
    print('=====================')
    print(fibonacci_lru(6))

