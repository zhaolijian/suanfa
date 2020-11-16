# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         head = None
#         # 存在至少一个链表为空
#         if pHead2 is None:
#             return pHead1
#         elif pHead1 is None:
#             return pHead2
#         else:
#             #  确定头节点
#             while pHead1 and pHead2:
#                 if pHead1.val >= pHead2.val:
#                     head = pHead2
#                     pHead2 = pHead2.next
#                 else:
#                     head = pHead1
#                     pHead1 = pHead1.next
#                 break
#             cur = head
#             while pHead1 and pHead2:
#                 if pHead1.val >= pHead2.val:
#                     cur.next = pHead2
#                     pHead2 = pHead2.next
#                     cur = cur.next
#                 else:
#                     cur.next = pHead1
#                     pHead1 = pHead1.next
#                     cur = cur.next
#             # 比较完只有一个链表不为空或者两个链表都为空
#             if pHead1:
#                 cur.next = pHead1
#             if pHead2:
#                 cur.next = pHead2
#         return head


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        elif pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         if not pHead1:
#             return pHead2
#         if not pHead2:
#             return pHead1
#         head = pHead1
#         if pHead1.val > pHead2.val:
#             head = pHead2
#             pHead2 = pHead2.next
#         else:
#             pHead1 = pHead1.next
#         cur = head
#         while pHead1 and pHead2:
#             if pHead1.val < pHead2.val:
#                 cur.next = pHead1
#                 cur = cur.next
#                 pHead1 = pHead1.next
#             else:
#                 cur.next = pHead2
#                 cur = cur.next
#                 pHead2 = pHead2.next
#         if not pHead1:
#             cur.next = pHead2
#         if not pHead2:
#             cur.next = pHead1
#         return head


if __name__ == '__main__':
    s = Solution()
    head1 = ListNode(1)
    cur1 = head1
    head2 = ListNode(4)
    cur2 = head2
    for i in range(2, 4):
        cur1.next = ListNode(i)
        cur1 = cur1.next
    for j in range(5, 7):
        cur2.next = ListNode(j)
        cur2 = cur2.next
    result = s.Merge(head1, head2)
    while result:
        print(result.val)
        result = result.next