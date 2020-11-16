# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
# 删除完毕后，请你返回最终结果链表的头节点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 两次遍历
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        d = {}
        sum = 0
        cur = dummy
        # 第一次遍历:记录累计和、该累计和最后一次出现节点对
        while cur:
            sum += cur.val
            d[sum] = cur
            cur = cur.next
        sum = 0
        cur = dummy
        # 第二次遍历,获得最终链表的头节点
        while cur:
            sum += cur.val
            cur.next = d[sum].next
            cur = cur.next
        return dummy.next



# 方法2 递归
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l = ListNode(0)
        l.next = head
        d = {0: l}
        s = 0
        while head:
            s += head.val
            if s in d:
                d[s].next = head.next
                # 递归构建
                return self.removeZeroSumSublists(l.next)
            else:
                d[s] = head
                head = head.next
        return l.next


if __name__ == '__main__':
    s = Solution()
    array = [3, 2, -3, -2, 5, 5, -5, 1]
    head = ListNode(1)
    cur = head
    for i in range(len(array)):
        cur.next = ListNode(array[i])
        cur = cur.next
    print(s.removeZeroSumSublists(head))