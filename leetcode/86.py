# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1 一次遍历，创建两个新链表
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        low, high = ListNode(0), ListNode(0)
        cur_low, cur_high = low, high
        cur = head
        while cur:
            if cur.val < x:
                cur_low.next = ListNode(cur.val)
                cur_low = cur_low.next
            else:
                cur_high.next = ListNode(cur.val)
                cur_high = cur_high.next
            cur = cur.next
        cur_low.next = high.next
        return low.next


# 方法2 两次遍历创建一个新链表
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(0)
        new_cur = new_head
        cur = head
        while cur:
            if cur.val < x:
                new_cur.next = ListNode(cur.val)
                new_cur = new_cur.next
            cur = cur.next
        cur = head
        while cur:
            if cur.val >= x:
                new_cur.next = ListNode(cur.val)
                new_cur = new_cur.next
            cur = cur.next
        return new_head.next


if __name__ == '__main__':
    s = Solution()
    dummy = ListNode(0)
    cur = dummy
    array = [1,4,3,2,5,2]
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    x = 3
    print(s.partition(dummy.next, x))