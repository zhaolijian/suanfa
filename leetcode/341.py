# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

import collections
class NestedIterator:
    def dfs(self, nests):
        for ele in nests:
            if ele.isInteger():
                self.queue.append(ele.getInteger())
            else:
                self.dfs(ele.getList())

    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return self.queue