# 方法1
# 用时间换空间,二分法
# 遍历数组,看小于n//2的元素个数,如果大于n//2-1,则在左边,否则在右边
class Solution:
    def findDuplicate(self, nums) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            number = 0
            for i in range(len(nums)):
                if l <= nums[i] <= mid:
                    number += 1
            if number > mid - l + 1:
                r = mid
            else:
                l = mid + 1
        return l


# 方法2
class Solution:
    def findDuplicate(self, nums) -> int:
        # 相当于有环链表
        # 1.设置快慢指针,找到相遇点
        low, fast = 0, 0
        while True:
            low = nums[low]
            fast = nums[nums[fast]]
            if low == fast:
                break

        # 2. 找到环入口点
        first, second = 0, low
        while True:
            if first == second:
                # 找到相遇点的索引，所以返回first，而不是nums[first]
                # 比如下面例子，索引为0-1-3-2-4-2-4-2-4。。。相遇点是索引2，但是重复的是索引2的索引，即3，索引3和索引4都指向2，索引重复的是索引3对应的值
                return first
            else:
                first = nums[first]
                second = nums[second]


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,4,2,2]
    print(s.findDuplicate(nums))