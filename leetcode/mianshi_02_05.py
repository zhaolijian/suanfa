# 链表求和
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 不使用额外空间，直接在原链表上修改
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 进位、10的倍数
        temp, tens = 0, 1
        h1, h2 = l1, l2
        # 使得l1为长链表，l2为短链表
        while h1 or h2:
            if not h1:
                l1, l2 = l2, l1
                break
            elif not h2:
                break
            else:
                h1 = h1.next
                h2 = h2.next
        cur1, cur2 = l1, l2
        # 记录l1的尾部值
        tail = l1
        while cur1:
            val1, val2 = 0, 0
            if not cur2:
                val1 = cur1.val
            else:
                val1, val2 = cur1.val, cur2.val
            sum_val = val1 + val2 + temp
            t1 = sum_val % 10
            temp = sum_val // 10
            cur1.val = t1
            tens *= 10
            tail = cur1
            if not cur2:
                cur1 = cur1.next
            else:
                cur1, cur2 = cur1.next, cur2.next
        if temp:
            tail.next = ListNode(temp)
        return l1


# 方法2 使用额外空间
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 进位、10的倍数
        temp, tens = 0, 1
        res = None
        cur = res
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            val1, val2 = 0, 0
            if not cur1:
                val2 = cur2.val
                cur2 = cur2.next
            elif not cur2:
                val1 = cur1.val
                cur1 = cur1.next
            else:
                val1, val2 = cur1.val, cur2.val
                cur1, cur2 = cur1.next, cur2.next
            sum_val = val1 + val2 + temp
            t1 = sum_val % 10
            temp = sum_val // 10
            if res is None:
                res = ListNode(t1)
                cur = res
            else:
                cur.next = ListNode(t1)
                cur = cur.next
            tens *= 10
        if temp:
            cur.next = ListNode(temp)
        return res


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    cur1 = l1.next
    cur1.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    cur2 = l2.next
    cur2.next = ListNode(4)
    print(s.addTwoNumbers(l1, l2))