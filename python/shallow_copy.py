list1 = [3, [66, 55, 44], (7, 8, 9)]
# shallow copy
list2 = list(list1)
assert list1 == list2
assert list1 is not list2

list1.append(100)
list1[1].remove(55)

print('list1:', list1)
print('list2:', list2)

list2[1] += [33, 22]
list2[2] += (10, 11)  # makes new tuple (7, 8, 9, 10, 11)

print('list1:', list1)
print('list2:', list2)
