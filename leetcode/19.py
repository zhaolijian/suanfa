class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        dummy = ListNode()
        dummy.next = head
        # slow到删除的节点,fast到最后一个节点
        slow, fast, prev, flag = dummy, dummy, None, True
        while fast.next:
            if flag:
                for i in range(n - 1):
                    fast = fast.next
                flag = False
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


# 繁琐些
# class Solution:
#     def removeNthFromEnd(self, head, n: int):
#         if not head:
#             return None
#         # 设置两个节点,一个指向头节点,一个指向第n个节点
#         index1 = head
#         index2 = head
#         temp = 0
#         while temp < n:
#             if index2 is None:
#                 return head
#             index2 = index2.next
#             temp += 1
#         if index2 is None:
#             return index1.next
#         cur = index1
#         while index2.next:
#             index2 = index2.next
#             cur = cur.next
#         cur.next = cur.next.next
#         return index1


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    cur = head
    temp = 2
    while temp <= 5:
        cur.next = ListNode(temp)
        cur = cur.next
        temp += 1
    print(s.removeNthFromEnd(head, 1))
