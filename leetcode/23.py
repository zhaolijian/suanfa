# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 分治法
class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, l, r):
        if not l:
            return r
        if not r:
            return l
        head = ListNode(0)
        cur = head
        while l and r:
            if l.val <= r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        if l:
            cur.next = l
        if r:
            cur.next = r
        return head.next


# 方法2 堆


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(4)
    cur1 = head1.next
    cur1.next = ListNode(5)
    head2 = ListNode(1)
    head2.next = ListNode(3)
    cur2 = head2.next
    cur2.next = ListNode(4)
    lists = [head1, head2]
    s = Solution()
    print(s.mergeKLists(lists))