# 用一个数组实现三个栈
class TripleInOne:

    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.array = [[0 for i in range(stackSize)] for j in range(3)]
        self.number = [0, 0, 0]

    def push(self, stackNum: int, value: int) -> None:
        length = self.number[stackNum]
        if length < self.stackSize:
            self.array[stackNum][length] = value
            self.number[stackNum] += 1
        else:
            return

    def pop(self, stackNum: int) -> int:
        length = self.number[stackNum]
        if length == 0:
            return -1
        else:
            temp = self.array[stackNum][length - 1]
            self.array[stackNum][length - 1] = 0
            self.number[stackNum] -= 1
            return temp

    def peek(self, stackNum: int) -> int:
        length = self.number[stackNum]
        if length == 0:
            return -1
        else:
            return self.array[stackNum][length - 1]

    def isEmpty(self, stackNum: int) -> bool:
        length = self.number[stackNum]
        if length == 0:
            return True
        return False