# 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
# 请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre_node, next_node = None, None
        dummy = ListNode(0, list1)
        cur = dummy
        number = 0
        while True:
            if number == a:
                pre_node = cur
            if number == b:
                next_node = cur.next.next
                break
            cur = cur.next
            number += 1
        pre_node.next = list2
        cur_list2 = list2
        while cur_list2.next:
            cur_list2 = cur_list2.next
        cur_list2.next = next_node
        return dummy.next