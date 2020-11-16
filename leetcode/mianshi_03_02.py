# 栈的最小值
class MinStack:

    def __init__(self):
        self.stack = []
        # 维护当前位置的最小值
        self.min_array = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_array:
            self.min_array.append(x)
        else:
            temp = self.min_array[-1]
            if temp < x:
                self.min_array.append(temp)
            else:
                self.min_array.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            self.min_array.pop()
            return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_array[-1]