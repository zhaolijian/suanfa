# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
# 0 <= key, value <= 106
# 最多调用 104 次 put、get 和 remove 方法

class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.length = 1009
        self.array = [None] * self.length

    def put(self, key: int, value: int) -> None:
        index = key % self.length
        if self.array[index] is None:
            self.array[index] = LinkedNode(key, value)
        head = self.array[index]
        prev = None
        while head:
            prev = head
            if head.key == key:
                head.val = value
                return
            head = head.next
        prev.next = LinkedNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.length
        head = self.array[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.length
        head = self.array[index]
        if head is None:
            return
        if head.key == key:
            self.array[index] = head.next
        prev, cur = head, head.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            cur = cur.next
            prev = prev.next

