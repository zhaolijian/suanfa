# 链表中倒数第k个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while k > 1:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow