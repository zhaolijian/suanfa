# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
#
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
#  
#
# 说明：
#
# 你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#  
#
# 进阶：
#
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。


# 方法1
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    # 放的时候直接放到stack1栈中即可
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    # 取的时候看看stack2中有没有元素，有的话直接取，如果没有的话，将stack1中的放到stack2中
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        temp = self.pop()
        self.stack2.append(temp)
        return temp


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2



# 方法2
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        # 直接调用pop方法即可，不用重写了
        temp = self.pop()
        self.stack2.append(temp)
        return temp


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2