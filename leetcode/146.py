# LRU缓存机制
class DLinkedList:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        # 使用伪头部节点和伪尾部节点，这样在删除尾部节点和添加头部节点时直接使用self.tail.prev和self.head.next定义
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        # 当前存储数量
        self.number = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        temp = self.cache[key]
        self.removeNode(temp)
        self.addToHead(temp)
        return temp.val

    def put(self, key: int, value: int) -> None:
        # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
        if key in self.cache:
            self.cache[key].val = value
            self.removeNode(self.cache[key])
            self.addToHead(self.cache[key])
        else:
            node = DLinkedList(key, value)
            self.cache[key] = node
            # 再添加则超出容量，先删除尾节点
            if self.number == self.capacity:
                temp = self.tail.prev
                self.removeNode(self.tail.prev)
                self.cache.pop(temp.key)
                self.number -= 1
            self.addToHead(node)
            self.number += 1

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node


if __name__ == '__main__':
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
    s.put(4, 4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))