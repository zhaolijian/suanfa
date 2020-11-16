# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        new_head = None
        while pHead:
            next = pHead.next
            pHead.next = new_head
            new_head = pHead
            pHead = next
        return new_head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    result = s.ReverseList(head)
    print(result.val)
