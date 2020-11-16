# 返回倒数第k个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def kthToLast(self, head: ListNode, k: int) -> int:
#         length = 0
#         cur = head
#         while cur:
#             length += 1
#             cur = cur.next
#         value = length - k + 1
#         cur = head
#         i = 1
#         while cur:
#             if i == value:
#                 return cur.val
#             else:
#                 i += 1
#                 cur = cur.next


# 快慢指针
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast, slow = head, head
        while k > 1:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.val


if __name__ == '__main__':
    s = Solution()
    k = 2
    head = ListNode(1)
    cur = head
    array = [2, 3, 4, 5]
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    print(s.kthToLast(head, k))