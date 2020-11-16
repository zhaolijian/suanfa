# 两个单链表找到第一个公共结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def func(self, headA, headB):
        temp1, temp2 = headA, headB
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
        return temp1


if __name__ == '__main__':
    s = Solution()
    headA = ListNode(1)
    curA = headA
    curA.next = ListNode(2)
    curA = curA.next
    curA.next = ListNode(3)
    headB = ListNode(0)
    curB = headB
    curB.next = ListNode(1)
    curB = curB.next
    curB.next = ListNode(3)
    print(s.func(headA, headB))