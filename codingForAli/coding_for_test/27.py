import collections
l = [1, 2, 3, 3, 4]
number = collections.Counter(l)
for key in number:
    print(key, number[key])