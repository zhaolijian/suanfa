# 方法1 使用堆的思想解决
import heapq
class Solution:
    def smallestRange(self, nums):
        array = []
        k = len(nums)
        min_val, max_val = float('inf'), float('-inf')
        # 每个数组取最小的元素放入栈中,并初始化min_val, max_val
        # 堆中存放每个子数组中的一个值，所以求每个堆的最小值和最大值，更新res即可
        for i in range(k):
            heapq.heappush(array, (nums[i][0], i, 0))
            min_val = min(min_val, nums[i][0])
            max_val = max(max_val, nums[i][0])
        res = [min_val, max_val]
        while True:
            temp = heapq.heappop(array)
            if temp[2] == len(nums[temp[1]]) - 1:
                break
            heapq.heappush(array, (nums[temp[1]][temp[2] + 1], temp[1], temp[2] + 1))
            min_val = array[0][0]
            max_val = max(max_val, nums[temp[1]][temp[2] + 1])
            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]
        return res

# 方法2 多指针遍历
class Solution:
    def smallestRange(self, nums):
        # define variables
        k = len(nums)
        index_list = [0] * k
        elem_list = [0] * k
        for i in range(k):
            elem_list[i] = nums[i][index_list[i]]
        minval, maxval = min(elem_list), max(elem_list)

        # recursion
        while True:
            currminval, currmaxval = min(elem_list), max(elem_list)
            if currmaxval - currminval < maxval - minval:
                maxval = currmaxval
                minval = currminval
            index = elem_list.index(currminval)
            if index_list[index] < len(nums[index]) - 1:
                index_list[index] += 1
                elem_list[index] = nums[index][index_list[index]]
            else:
                break
        return [minval, maxval]


if __name__ == '__main__':
    s = Solution()
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print(s.smallestRange(nums))