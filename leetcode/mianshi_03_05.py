# 栈排序
class SortedStack:

    def __init__(self):
        self.stack = []
        self.stack1 = []


    def push(self, val: int) -> None:
        while self.stack1:
            self.stack.append(self.stack1.pop())
        while self.stack and self.stack[-1] < val:
            self.stack1.append(self.stack.pop())
        self.stack.append(val)


    def pop(self) -> None:
        if not self.stack and not self.stack1:
            return -1
        while self.stack1:
            self.stack.append(self.stack1.pop())
        return self.stack.pop()


    def peek(self) -> int:
        if not self.stack and not self.stack1:
            return -1
        while self.stack1:
            self.stack.append(self.stack1.pop())
        return self.stack[-1]


    def isEmpty(self) -> bool:
        return True if not self.stack and not self.stack1 else False