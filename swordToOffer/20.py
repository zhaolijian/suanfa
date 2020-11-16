# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        # 用于存放对应栈元素所在位置及之前元素最小值
        self.assist = []

    def push(self, node):
        if len(self.assist) == 0 or node < self.assist[-1]:
            self.assist.append(node)
        else:
            self.assist.append(self.min())
        self.stack.append(node)

    def pop(self):
        self.assist.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.assist[-1]



class Solution:
    def __init__(self):
        self.stack = []
        # 用来存放最小值
        self.assist = []

    def push(self, node):
        self.stack.append(node)
        if not self.assist or self.assist[-1] >= node:
            self.assist.append(node)

    def pop(self):
        if self.assist[-1] == self.stack[-1]:
            self.assist.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.assist[-1]



if __name__ == '__main__':
    s = Solution()
    s.push(3)
    print(s.stack)
    print(s.assist)
    print(s.min())
    s.push(4)
    print(s.stack)
    print(s.assist)
    print(s.min())
    s.push(2)
    print(s.stack)
    print(s.assist)
    print(s.min())
    s.push(3)
    print(s.stack)
    print(s.assist)
    print(s.min())
    s.pop()
    print(s.stack)
    print(s.assist)
    print(s.min())
    s.pop()
    print(s.stack)
    print(s.assist)
    print(s.min())
