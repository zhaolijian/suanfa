# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # 如果l1是短链表则交换
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        if cur2:
            l1, l2 = l2, l1
        head1, head2 = l1, l2
        temp = 0
        # 记录l1的尾节点
        tail = head1
        while head1 or head2:
            val2 = head2.val if head2 else 0
            if head1.val + val2 + temp < 10:
                head1.val += (val2 + temp)
                temp = 0
            else:
                head1.val = head1.val + val2 + temp - 10
                temp = 1
            tail = head1
            head1 = head1.next
            head2 = head2.next if head2 else None
        if temp:
            tail.next = ListNode(1)
        return l1