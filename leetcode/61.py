# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        cur = head
        tail = None
        while cur:
            length += 1
            tail = cur
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        pre = None
        new_head = head
        for i in range(length - k):
            pre = new_head
            new_head = new_head.next
        pre.next = None
        tail.next = head
        return new_head


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if k % length == 0:
            return head
        # 指针移动的步数
        k = length - k % length
        dummy = ListNode(0)
        dummy.next = head
        last, cur = dummy, dummy.next
        while k:
            last = last.next
            cur = cur.next
            k -= 1
        last.next = None
        tail = cur
        while tail.next:
            tail = tail.next
        tail.next = dummy.next
        dummy.next = cur
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    array = [1, 2, 3, 4, 5]
    dummy = ListNode(0)
    cur = dummy
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    k = 2
    print(s.rotateRight(dummy.next, k))