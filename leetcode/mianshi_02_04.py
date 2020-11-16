# 分割链表，小于数x的放前面
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 双指针
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        p, q = head, head
        while q:
            if q.val < x:
                p.val, q.val = q.val, p.val
                p = p.next
            q = q.next
        return head


# 方法2 头插法
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        # 找到第一个大于等于x的节点
        first = None
        cur = head
        # first节点之后的小于x的节点值
        array = []
        while cur:
            if cur.val >= x:
                first = cur
                break
            else:
                cur = cur.next
        if first is None:
            return head
        current = first
        while current.next:
            temp = current.next
            if temp.val < x:
                array.append(temp.val)
                current.next = temp.next
            else:
                current = current.next
        for ele in array:
            temp = ListNode(ele)
            temp.next = head
            head = temp
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    array = [4, 3, 2, 5, 2]
    cur = head
    for i in range(5):
        cur.next = ListNode(array[i])
        cur = cur.next
    x = 3
    print(s.partition(head, x))