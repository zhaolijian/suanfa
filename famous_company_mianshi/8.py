# 给定一个链表，删除链表的倒数第n个节点并返回链表的头指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self , head , n ):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next