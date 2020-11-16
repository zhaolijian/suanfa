# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 将链表中的所有节点存放在一个数组中，遍历链表中的所有节点，如果节点出现在数组中，则返回,复杂度高
# class Solution:
#     def EntryNodeOfLoop(self, pHead):
#         if not pHead or not pHead.next:
#             return None
#         init = []
#         while pHead:
#             if pHead in init:
#                 return pHead
#             else:
#                 init.append(pHead)
#             pHead = pHead.next
#         return None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None
        # 两个指针,一个速度为2,一个速度为1,记录最终相遇点
        # 两个节点,一个从链表头出发,一个从相遇点出发,最后一定会相遇
        index1, index2 = pHead, pHead
        common = None
        while index1:
            index1 = index1.next
            index2 = index2.next.next
            if index1 == index2:
                common = index1
                break
        p1, p2 = pHead, common
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


if __name__ == '__main__':
    head = ListNode(1)
    temp = head
    m = 2
    while m <= 5:
        head.next = ListNode(m)
        head = head.next
        m += 1
    head.next = temp
    s = Solution()
    print(s.EntryNodeOfLoop(temp).val)
