# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_array = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_array:
            self.min_array.append(x)
        else:
            self.min_array.append(x if x < self.min_array[-1] else self.min_array[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_array.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_array[-1]

