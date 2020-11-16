# 链表找交点
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def func(self, head1, head2):
        stack1, stack2 = [], []
        while head1:
            stack1.append(head1)
            head1 = head1.next
        while head2:
            stack2.append(head2)
            head2 = head2.next
        res = None
        while stack1 and stack2:
            temp1 = stack1.pop()
            temp2 = stack2.pop()
            if temp1.val == temp2.val:
                res = temp1
        return res


if __name__ == '__main__':
    s = Solution()
    head1 = LinkedList(1)
    head1.next = LinkedList(3)
    cur1 = head1.next
    cur1.next = LinkedList(4)

    head2 = LinkedList(2)
    head2.next = LinkedList(3)
    cur2 = head2.next
    cur2.next = LinkedList(4)
    print(s.func(head1, head2).val)