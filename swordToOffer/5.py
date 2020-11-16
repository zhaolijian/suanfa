# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(node)

    def pop(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    s = Solution()
    s.push(2)
    print(s.stack1)
    print(s.stack2)
    s.push(3)
    print(s.stack1)
    print(s.stack2)
    result = s.pop()
    print(s.stack1)
    print(s.stack2)
    print(result)