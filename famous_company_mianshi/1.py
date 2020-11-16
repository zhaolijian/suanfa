# LRU缓存
class DoubleLinked:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def LRU(self, operators, k):
        d = {}
        number = 0
        res = []
        head = DoubleLinked()
        tail = DoubleLinked()
        head.next = tail
        tail.prev = head

        def removeNode(node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def addTotail(node):
            tail.prev.next = node
            node.prev = tail.prev
            node.next = tail
            tail.prev = node

        def set(key, val):
            if key in d:
                removeNode(d[key])
                d[key].val = val
                addTotail(d[key])
            else:
                nonlocal number
                if number == k:
                    temp = head.next
                    removeNode(temp)
                    d.pop(temp.key)
                    number -= 1
                new_node = DoubleLinked(key, val)
                addTotail(new_node)
                d[key] = new_node
                number += 1

        def get(key):
            if key in d:
                temp = d[key]
                removeNode(temp)
                addTotail(temp)
                return temp.val
            else:
                return -1

        for i in range(len(operators)):
            if operators[i][0] == 1:
                set(operators[i][1], operators[i][2])
            elif operators[i][0] == 2:
                res.append(get(operators[i][1]))
        return res


if __name__ == '__main__':
    s = Solution()
    operations = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
    k = 3
    print(s.LRU(operations, k))