# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
# 返回同样按升序排列的结果链表。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法1
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next.val
                while cur.next and cur.next.val == temp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


# 方法2 哈希表
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 统计没有重复出现的数字
        s = defaultdict(int)
        cur = head
        while cur:
            s[cur.val] += 1
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if s[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    array = [1, 1, 2, 3]
    cur = head
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    print(s.deleteDuplicates(head))