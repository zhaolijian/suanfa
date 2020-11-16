# 痛排序
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        ct = Counter(tasks)
        # 出现次数最多的一个组成一个list，选择list中的第一个，选择list中第一个元素的第二个位置
        # Counter('abcdeabcdabcaba').most_common(3)
        # [('a', 5), ('b', 4), ('c', 3)]
        # 出现最多的次数
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))


if __name__ == '__main__':
    s = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(s.leastInterval(tasks, n))
