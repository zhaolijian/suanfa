# 两个链表合并称一个新链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        # write code here
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(1)
    print(s.mergeTwoLists(l1, l2))