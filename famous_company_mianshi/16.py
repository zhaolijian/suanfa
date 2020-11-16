# 将一个链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 ，空间复杂度 。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1 简单明了
class Solution:
    def reverseBetween(self , head , m , n ):
        # write code here
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        for i in range(1, m):
            pre = pre.next
            cur = cur.next
        for j in range(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next


# 方法2 太繁琐了
# class Solution:
#     def reverseBetween(self , head , m , n ):
#         if m == n:
#             return head
#         h = head
#         dummy = ListNode(0)
#         dummy.next = head
#         last_tail = dummy
#         cur = head
#         i = 1
#         while i < n:
#             if i < m:
#                 last_tail = cur
#             if i == m:
#                 h = cur
#             cur = cur.next
#             i += 1
#         next_head = cur.next
#         tail = cur
#         tail.next = None
#         mid_head, mid_cur = None, h
#         mid_tail = mid_cur
#         while mid_cur:
#             temp = mid_cur.next
#             mid_cur.next = mid_head
#             mid_head = mid_cur
#             mid_cur = temp
#         last_tail.next = mid_head
#         mid_tail.next = next_head
#         return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    cur = head
    array = [2, 3, 4, 5]
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    m = 2
    n = 4
    # head = ListNode(3)
    # head.next = ListNode(5)
    # m = 2
    # n = 2
    print(s.reverseBetween(head, m, n))