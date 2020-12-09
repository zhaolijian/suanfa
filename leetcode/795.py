# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
# 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。


# 不大于R+1的子数组的个数 - 不大于L的子数组个数即为所求
class Solution:
    def numSubarrayBoundedMax(self, A, L: int, R: int) -> int:
        def notGreater(number):
            res = 0
            temp = 0
            for ele in A:
                if ele < number:
                    temp += 1
                else:
                    temp = 0
                res += temp
            return res
        return notGreater(R + 1) - notGreater(L)


if __name__ == '__main__':
    s = Solution()
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    print(s.numSubarrayBoundedMax(A, L, R))