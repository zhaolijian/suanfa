# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
# 如果可以完成上述分割，则返回 true ；否则，返回 false 。


# 方法1 哈希表+最小堆，时间复杂度O(nlogn)
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def isPossible(self, nums) -> bool:
        # 键是子序列的最后一个值，值是最大值为键的子序列长度组成的最小堆
        d = defaultdict(list)
        for ele in nums:
            if d[ele - 1]:
                temp = heappop(d[ele - 1])
                heappush(d[ele], temp + 1)
            else:
                heappush(d[ele], 1)
        return not any(d[key] and d[key][0] < 3 for key in d.keys())


# 方法2， 哈希表 时间复杂度O(n)
from collections import Counter
class Solution:
    def isPossible(self, nums) -> bool:
        # 元素剩余个数
        c = Counter(nums)
        # 用来存放以某个元素结尾的数组长度大于等于3的数组个数
        tail = Counter()
        for ele in nums:
            if not c[ele]:
                continue
            # 这两个elif不能调换，因为要优先使得子序列长度变得更长，原因没懂
            elif c[ele] and tail[ele - 1]:
                c[ele] -= 1
                tail[ele - 1] -= 1
                tail[ele] += 1
            elif c[ele] and c[ele + 1] and c[ele + 2]:
                c[ele] -= 1
                c[ele + 1] -= 1
                c[ele + 2] -= 1
                tail[ele + 2] += 1
            else:
                return False
        return True


# 方法3 双循环遍历， 时间复杂度O(n^2)
class Solution:
    def isPossible(self, nums) -> bool:
        array = []
        for ele in nums:
            flag = False
            for sub in array[::-1]:
                if ele == sub[-1] + 1:
                    sub.append(ele)
                    flag = True
                    break
            if not flag:
                array.append([ele])
        return True if all(len(sub) >= 3 for sub in array) else False
