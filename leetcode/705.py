# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 0 <= key <= 106
# 最多调用 104 次 add、remove 和 contains 。


# 方法1 有了哈希表中存储数据的取值范围，可以创建一个数组
# class MyHashSet:
#
#     def __init__(self):
#         self.b = [False] * 1000001
#
#     def add(self, key: int) -> None:
#         self.b[key] = True
#
#     def remove(self, key: int) -> None:
#         self.b[key] = False
#
#     def contains(self, key: int) -> bool:
#         return self.b[key]


# 方法2 链地址法
class linkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyHashSet:

    def __init__(self):
        self.length = 1009
        self.array = [[]] * self.length

    def add(self, key: int) -> None:
        index = key % self.length
        head = self.array[index]
        if not head:
            self.array[index] = linkedNode(key)
            return
        tail = None
        while head:
            tail = head
            if head.val == key:
                return
            head = head.next
        tail.next = linkedNode(key)

    def remove(self, key: int) -> None:
        index = key % self.length
        head = self.array[index]
        if not head:
            return
        if head.val == key:
            self.array[index] = head.next
            return
        prev, cur = head, head.next
        while cur:
            if cur.val == key:
                prev.next = cur.next
                return
            prev = prev.next
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % self.length
        head = self.array[index]
        while head:
            if head.val == key:
                return True
            head = head.next
        return False


class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 该方法超时，可能是由于初始化[LinkedNode(-1)] * self.length花费的时间太长了
class MyHashSet:
    def __init__(self):
        self.length = 1009
        self.array = [LinkedNode(-1)] * self.length

    def add(self, key: int) -> None:
        if not self.contains(key):
            dummy = self.array[key % self.length]
            insert_node = LinkedNode(key)
            insert_node.next = dummy.next
            dummy.next = insert_node

    def remove(self, key: int) -> None:
        prev = self.array[key % self.length]
        cur = prev.next
        while cur:
            if cur.val == key:
                prev.next = cur.next
                return
            prev = prev.next
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.array[key % self.length].next
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    s = MyHashSet()
    print(s.add(1))
    print(s.add(2))
    print(s.contains(1))
    print(s.contains(3))
    print(s.add(2))
    print(s.contains(2))
    print(s.remove(2))
    print(s.contains(2))