# 反转链表
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        head, cur = None, pHead
        while cur:
            temp = cur.next
            cur.next = head
            head = cur
            cur = temp
        return head