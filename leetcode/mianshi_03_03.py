# 堆盘子
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stack = []

    # 即使前面的栈中不满，也不填充，还是在最后的栈填充或者增加新的栈，题目表述不清
    def push(self, val: int) -> None:
        if self.cap <= 0:
            return -1
        if not self.stack or len(self.stack[-1]) == self.cap:
            self.stack.append([val])
        else:
            self.stack[-1].append(val)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.stack[-1]) == 1:
            temp = self.stack[-1][0]
            self.stack.pop()
            return temp
        else:
            return self.stack[-1].pop()

    def popAt(self, index: int) -> int:
        if index >= len(self.stack):
            return -1
        length = len(self.stack[index])
        if length == 1:
            temp = self.stack[index][0]
            self.stack.pop(index)
            return temp
        else:
            return self.stack[index].pop()


if __name__ == '__main__':
    s = StackOfPlates(1)
    s.push(1)
    s.push(2)
    s.popAt(1)
    s.pop()
    s.pop()