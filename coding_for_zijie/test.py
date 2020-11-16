import heapq
# 虽然显示红色，但是可以运行
from heapq import _heapify_max, _heappop_max, _heapreplace_max

list = [1, 2, 3]
_heapify_max(list)
print(list)
print(_heappop_max(list))
print(list)
print(_heapreplace_max(list, 3))
print(list)
