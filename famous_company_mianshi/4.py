# 判断链表有没有环
class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self , head ):
        if not head or not head.next:
            return False
        slow, fast = head, head.next.next
        while fast and fast.next:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        return True if slow == fast and slow else False


if __name__ == '__main__':
    s = Solution()
    head = LinkedList(1)
    head.next = LinkedList(2)
    print(s.hasCycle(head))