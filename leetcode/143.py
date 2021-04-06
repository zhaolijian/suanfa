# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_node, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = second_node
            second_node = cur
            cur = temp
        l1, l2 = head, second_node
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l1 = temp1
            l2.next = l1
            l2 = temp2