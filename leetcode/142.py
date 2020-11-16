class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        new_head = head
        # 说明有环
        if fast and fast.next:
            while new_head != fast:
                new_head = new_head.next
                fast = fast.next
            return new_head
        return None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        first, second = head, head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                break
        if not second or not second.next:
            return None
        new_head = head
        while new_head != second:
            new_head = new_head.next
            second = second.next
        return new_head


if __name__ == '__main__':
    s = Solution()
    l = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    # l = [1,2,3]
    head = ListNode(l[0])
    cur = head
    temp = None
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
        if i == 24:
            temp = cur
    cur.next = temp
    print(s.detectCycle(head).val)