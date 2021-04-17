# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while prev and prev.next and prev.next.next:
            cur = prev.next
            next_node = prev.next.next
            prev.next = next_node
            cur.next = next_node.next
            next_node.next = cur
            prev = cur
        return dummy.next