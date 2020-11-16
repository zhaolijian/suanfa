# 环路检测
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        mid = slow
        temp = head
        while mid != temp:
            mid = mid.next
            temp = temp.next
        return mid


if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    cur = head
    cur.next = ListNode(2)
    cur = cur.next
    temp = cur
    cur.next = ListNode(0)
    cur = cur.next
    cur.next = ListNode(4)
    cur = cur.next
    cur.next = temp
    print(s.detectCycle(head))