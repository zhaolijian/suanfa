# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visisted = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if head in self.visisted:
            return self.visisted[head]
        new_head = Node(head.val)
        self.visisted[head] = new_head
        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.copyRandomList(head.random)
        return new_head