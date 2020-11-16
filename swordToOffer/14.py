# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入一个链表，输出该链表中倒数第k个结点。
# 方法1：获取链表长度，从而可以得到倒数第k个节点是正数第多少个
# 方法2：将链表逆序，原倒数第k个节点，即正数第k个节点
# class Solution:
#     def FindKthToTail(self, head, k):
#         # 链表节点总数
#         number = 0
#         cur = head
#         while cur:
#             number += 1
#             cur = cur.next
#         # 倒数第k个节点在链表中正数第多少个
#         index = number - k
#         if index < 0:
#             return None
#         temp = head
#         while index > 0:
#             temp = temp.next
#             index -= 1
#         return temp


# 使用栈的思想，将链表中的所有节点放入栈中，取第k的节点
class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        init = []
        number = 0
        while head:
            init.append(head)
            head = head.next
            number += 1
        if k > number:
            return None
        return init[-k]

# 方法2，设置两个指针，一个先走k-1步，然后两个同时走，当先走的到达链表尾步时，另一个到达倒数第k个
class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        temp1 = head
        temp2 = head
        while k > 1:
            if temp1.next is not None:
                temp1 = temp1.next
                k -= 1
            else:
                return None
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next
        return temp2


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    s = Solution()
    node = s.FindKthToTail(head, 2)
    print(node)
    print(node.val)
