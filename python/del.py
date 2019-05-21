#encoding=utf-8
import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('bye...')

# s1 이 가리키는 튜플이 제거되면 (s1 finalize) bye가 불린다 (callback)
# finalize는 튜플에 대해 'weak reference' 를 가진다
ender = weakref.finalize(s1, bye)
assert ender.alive is True

del s1  # 튜플을 가리키는 변수 둘 중 하나 제거

assert ender.alive is True

s2 = 'spam'  # 마지막 튜플을 가리키는 변수 제거
# bye... printed

assert ender.alive is False
