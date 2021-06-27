# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value 需要返回 -1


# 单调递减队列
class MaxQueue:

    def __init__(self):
        self.array = []
        self.max_values = []

    def max_value(self) -> int:
        return -1 if not self.max_values else self.max_values[0]

    def push_back(self, value: int) -> None:
        while self.max_values and self.max_values[-1] < value:
            self.max_values.pop()
        self.max_values.append(value)
        self.array.append(value)

    def pop_front(self) -> int:
        if not self.array:
            return -1
        # 要删除的元素
        temp = self.array.pop(0)
        if temp == self.max_values[0]:
            self.max_values.pop(0)
        return temp
