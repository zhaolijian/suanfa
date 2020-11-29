# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 你需要返回给定数组中的重要翻转对的数量。


# 归并排序法
class Solution:
    def reversePairs(self, nums) -> int:
        res = 0

        def func(nums):
            nonlocal res
            length = len(nums)
            if length < 2:
                return nums
            mid = length // 2
            l = func(nums[:mid])
            r = func(nums[mid:])
            i, j = 0, 0
            # 计算重要反转对数量（本来打算和归并放一块，发现不太好做）
            n = 0
            for m in range(mid):
                while n < length - mid and l[m] > 2 * r[n]:
                    n += 1
                res += n
            array = []
            while i < mid and j < length - mid:
                if l[i] > r[j]:
                    array.append(r[j])
                    j += 1
                else:
                    array.append(l[i])
                    i += 1
            if i < mid:
                array += l[i:]
            if j < length - mid:
                array += r[j:]
            return array

        func(nums)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,2,3,1]
    print(s.reversePairs(nums))