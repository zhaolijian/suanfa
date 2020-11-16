class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def deleteDuplication(self, pHead):
        # 添加一个头节点，可以避免第一、第二个节点相同的情况
        head = ListNode(0)
        head.next = pHead
        # 当前节点
        pre = head
        # 探索节点
        last = head.next
        while last:
            if last.next and last.val == last.next.val:
                while last.next and last.val == last.next.val:
                    last = last.next
                pre.next = last.next
                last = last.next
            else:
                pre = last.next
                last = last.next
        return head.next
