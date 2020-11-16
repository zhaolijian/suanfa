# 用队列实现栈
# 单队列
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        length = len(self.queue)
        while length > 1:
            self.queue.append(self.queue.pop(0))
            length -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# 双队列
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array1 = []
        self.array2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.array1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        length = len(self.array1)
        while length > 1:
            self.array2.append(self.array1.pop(0))
            length -= 1
        self.array1, self.array2 = self.array2, self.array1
        return self.array2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        temp = self.pop()
        self.array1.append(temp)
        return temp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.array1


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.pop()
    param_5 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)