# 数组中的第K个最大元素
import heapq


# 构建最小堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        array = nums[:k]
        heapq.heapify(array)
        for i in range(k, len(nums)):
            heapq.heappushpop(array, nums[i])
        return array[0]


# 上面使用heappushpop方法更简洁
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = nums[:k]
        heapq.heapify(temp)
        for i in range(k, len(nums)):
            if temp[0] < nums[i]:
                heapq.heapreplace(temp, nums[i])
        return temp[0]