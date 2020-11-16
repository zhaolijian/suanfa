# 设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
# 注意: 允许出现重复元素。
# insert(val)：向集合中插入元素 val。
# remove(val)：当 val 存在时，从集合中移除一个 val。
# getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。


from collections import defaultdict
from random import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 数组
        self.array = []
        # 字典
        self.d = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.array.append(val)
        if val not in self.d:
            self.d[val] = {len(self.array) - 1}
            return True
        else:
            self.d[val].add(len(self.array) - 1)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # 如果要删除的位置是数组中最后一个位置,则删除数组中的最后一个位置,返回true
        # 如果数组中最后一个位置元素和要删除的位置元素不一致,则将最后一个元素值放在要删除的位置上,并更新原先最后一个位置值的字典set索引
        if val not in self.d:
            return False
        # 删除的位置
        index = self.d[val].pop()
        # 如果删除后没有该元素了，则从字典中删除
        if not self.d[val]:
            self.d.pop(val)
        # 如果删除的位置为数组中的最后一个位置,则删除数组中的最后一个元素即可
        if index == len(self.array) - 1:
            self.array.pop()
        # 如果删除的位置不是数组中的最后一个位置
        else:
            self.array[index] = self.array[-1]
            last_val = self.array.pop()
            self.d[last_val].remove(len(self.array))
            self.d[last_val].add(index)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.array)


if __name__ == '__main__':
    collection = RandomizedCollection()
    collection.insert(1)
    collection.remove(1)
    collection.insert(1)