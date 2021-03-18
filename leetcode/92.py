# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 头插法
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        init = ListNode(0)
        init.next = head
        # m位置前一个节点,m位置节点
        p, q = init, head
        for i in range(m - 1):
            p = p.next
            q = q.next
        for i in range(n - m):
            temp = q.next
            q.next = q.next.next
            temp.next = p.next
            p.next = temp
        return init.next



# 方法2 链表反转
class Solution:
    def reverseBetween(self, head, m, n):
        init = ListNode(0)
        init.next = head
        last_node = init
        mid_head, mid_tail = init.next, None
        cur = head
        for i in range(m - 1):
            mid_head = mid_head.next
            last_node = last_node.next
        mid_tail = mid_head
        cur = mid_head.next
        for i in range(n - m):
            temp = cur.next
            cur.next = mid_head
            mid_head = cur
            cur = temp
        last_node.next = mid_head
        mid_tail.next = cur
        return init.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    array = [2, 3, 4, 5]
    cur = head
    for ele in array:
        cur.next = ListNode(ele)
        cur = cur.next
    print(s.reverseBetween(head, 2, 4))