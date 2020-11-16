# 5,[[2,4],[1,4],[0,3],[0,3]]
# 5 3 1 2 4
# 2 3 1 5 4
# 求前面比后面小的逆序对
# 给一个降序的数组，例如给数字是5 ，数组就是 【5，4，3，2，1】 给一串交换指令 【【2，4】 【0，1】】，得到结果是【1，5，3，2，4】，
# 那么它的逆序的值就是（1，5），（1，4），（2，4），（3，4），（1，3）那么逆序值就是4。
class Solution:
    def __init__(self):
        self.res = 0

    def determine_virus_type(self , size , swap_indexes ):
        def func(nums):
            length = len(nums)
            if length <= 1:
                return nums
            mid = length // 2
            left = func(nums[:mid])
            right = func(nums[mid:])
            result = []
            i, j = 0, 0
            len_l, len_r = len(left), len(right)
            while i < len_l and j < len_r:
                if left[i] >= right[j]:
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    self.res += len_r - j
                    i += 1
            if i < len_l:
                result += left[i:]
            if j < len_r:
                result += right[j:]
            return result

        init = [i for i in range(size, 0, -1)]
        for i, j in swap_indexes:
            init[i], init[j] = init[j], init[i]
        func(init)
        return 1 if self.res % 2 else 2


if __name__ == '__main__':
    s = Solution()
    size = 5
    swap_indexes = [[2,4],[1,4],[0,3]]
    print(s.determine_virus_type(size, swap_indexes))