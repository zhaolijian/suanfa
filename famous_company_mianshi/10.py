class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addInList(self, head1, head2):
        def reverse(node):
            head, cur = None, node
            length = 0
            while cur:
                temp = cur.next
                cur.next = head
                head = cur
                cur = temp
                length += 1
            return head, length, node

        head1, len_1, w1 = reverse(head1)
        head2, len_2, w2 = reverse(head2)
        if len_1 < len_2:
            head1, head2 = head2, head1
        cur1, cur2 = head1, head2
        last_node = ListNode(0)
        last_node.next = head1
        temp = 0
        while cur1 or cur2:
            val2 = 0 if not cur2 else cur2.val
            val1 = cur1.val
            cur_val = val1 + val2 + temp
            cur1.val = cur_val % 10
            temp = cur_val // 10
            cur1 = cur1.next
            cur2 = cur2.next if cur2 else None
            last_node = last_node.next
        if temp == 1:
            last_node.next = ListNode(1)
        res, length, node = reverse(head1)
        return res


if __name__ == '__main__':
    s = Solution()
    head1 = ListNode(9)
    head1.next = ListNode(3)
    cur1 = head1.next
    cur1.next = ListNode(7)

    head2 = ListNode(6)
    head2.next = ListNode(3)
    print(s.addInList(head1, head2))