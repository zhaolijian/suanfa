s = set()
s.add((1, 2, 3))
s.add((2, 3, 4))
s.add((2, 3, 5))
new = list(map(list, s))
print(new)