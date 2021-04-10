# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶：
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 栈
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        cur1, cur2 = l1, l2
        while cur1:
            stack1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            stack2.append(cur2.val)
            cur2 = cur2.next
        # 链表采用头插法
        dummy = ListNode(0)
        # 进位
        number = 0
        while stack1 or stack2 or number:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            val = val1 + val2 + number
            number = val // 10
            insertNode = ListNode(val % 10)
            insertNode.next = dummy.next
            dummy.next = insertNode
        return dummy.next


# 方法2  这种方法也可以不修改输入链表，时间复杂度和空间复杂度较高
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 首先获取l1和l2的长度
        len1, len2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            if cur1:
                len1 += 1
                cur1 = cur1.next
            if cur2:
                len2 += 1
                cur2 = cur2.next
        # 创建一个存储对应位加和的数组
        array = [0] * max(len1, len2)
        cur1, cur2, index = l1, l2, 0
        if len1 > len2:
            for i in range(len1 - len2):
                array[index] = cur1.val
                cur1 = cur1.next
                index += 1
        if len2 > len1:
            for i in range(len2 - len1):
                array[index] = cur2.val
                cur2 = cur2.next
                index += 1
        while cur1 and cur2:
            val1, val2 = cur1.val, cur2.val
            cur1 = cur1.next
            cur2 = cur2.next
            array[index] = val1 + val2
            index += 1
        # 表示进位
        number = 0
        if array[-1] >= 10:
            number = 1
            array[-1] %= 10
        for i in range(max(len1, len2) - 2, -1, -1):
            new_val = number + array[i]
            number = new_val // 10
            array[i] = new_val % 10
        if number > 0:
            array = [number] + array
        dummy = ListNode(0)
        cur = dummy
        for ele in array:
            cur.next = ListNode(ele)
            cur = cur.next
        return dummy.next


# 方法3 反转链表
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_l1 = self.reverseNode(l1)
        new_l2 = self.reverseNode(l2)
        dummy = ListNode(0)
        cur = dummy
        # 进位
        number = 0
        while new_l1 or new_l2:
            val1, val2 = 0, 0
            if new_l1:
                val1 = new_l1.val
                new_l1 = new_l1.next
            if new_l2:
                val2 = new_l2.val
                new_l2 = new_l2.next
            sum_val = val1 + val2 + number
            number = sum_val // 10
            sum_val = sum_val % 10
            cur.next = ListNode(sum_val)
            cur = cur.next
        if number != 0:
            cur.next = ListNode(number)
        return self.reverseNode(dummy.next)

    def reverseNode(self, head):
        new_head, cur = None, head
        while cur:
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp
        return new_head
