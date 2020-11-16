# 回文链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 反转后半部分链表，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 从slow开始反转链表
        pre, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True


# 下面这种方法的反转链表用的较少，用上面的常用的反转链表的方法即可
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # 从slow开始反转链表
#         pre = slow
#         while slow and slow.next:
#             tmp = slow.next.next
#             slow.next.next = pre
#             pre = slow.next
#             slow.next = tmp
#         while pre and head:
#             if pre.val != head.val:
#                 return False
#             pre = pre.next
#             head = head.next
#         return True


if __name__ == '__main__':
    s = Solution()
    # head = ListNode(1)
    # head.next = ListNode(2)
    # cur = head.next
    # cur.next = ListNode(2)
    # cur = cur.next
    # cur.next = ListNode(1)

    head = ListNode(1)
    head.next = ListNode(0)
    cur = head.next
    cur.next = ListNode(1)

    print(s.isPalindrome(head))