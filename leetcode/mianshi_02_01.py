# 移除链表中的重复节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return None
        set_array = set()
        set_array.add(head.val)
        temp = head
        cur = head.next
        while cur:
            if cur.val not in set_array:
                temp.next = cur
                temp = temp.next
                set_array.add(cur.val)
            cur = cur.next
        return head


# 原地修改
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # set_array = set()
        # set_array.add(head.val)
        # 用该句代替也行 set_array = {head.val} 初始化不为空的set集合
        temp = head
        while temp.next:
            cur = temp.next
            if cur.val not in set_array:
                set_array.add(cur.val)
                temp = temp.next
            else:
                temp.next = temp.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    cur = head
    array = [2, 3, 3, 2, 1]
    for i in range(5):
        cur.next = ListNode(array[i])
        cur = cur.next
    print(s.removeDuplicateNodes(head))