# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 方法1 最小堆，最佳算法
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        list = []
        res = []
        heapq.heapify(list)
        i = 0
        for key, val in c.items():
            if i < k:
                heapq.heappush(list, (val, key))
                i += 1
            else:
                heapq.heappushpop(list, (val, key))
        while list:
            res.append(heapq.heappop(list)[1])
        return res



# 方法2 桶排序:次数当作桶，里面存放值
from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        array = defaultdict(list)
        for key, val in d.items():
            array[val].append(key)
        res = []
        temp = 0
        for i in range(len(nums), 0, -1):
            if i in array:
                for j in array[i]:
                    res.append(j)
                    temp += 1
                    if temp >= k:
                        return res


# 方法3 和上面方法类似
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = Counter(nums)
        array = []
        for key, val in c.items():
            array.append((val, key))
        array.sort(key=lambda x: x[0], reverse=True)
        for val, key in array:
            res.append(key)
            if len(res) >= k:
                return res