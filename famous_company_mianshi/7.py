# 对于一个给定的链表，返回环的入口节点，如果没有环，返回null
class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self , head):
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        if slow != fast:
            return None
        new_node = head
        while slow != new_node:
            slow = slow.next
            new_node = new_node.next
        return new_node

class Solution:
    def detectCycle(self , head):
        if not head or not head.next:
            return None
        # 与上面方法对比，下面几行不同
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        new_head = head
        while new_head != slow:
            new_head = new_head.next
            slow = slow.next
        return new_head


if __name__ == '__main__':
    s = Solution()
    head = LinkedNode(1)
    head.next = LinkedNode(2)
    cur = head.next
    temp = cur
    cur.next = LinkedNode(3)
    cur = cur.next
    cur.next = LinkedNode(4)
    cur = cur.next
    cur.next = temp
    print(s.detectCycle(head))