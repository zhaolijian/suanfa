# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
# 现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 说明: 请尽可能地优化你算法的时间和空间复杂度。


# 大佬的简洁代码
class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))


# 自己的
class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 数组、剩下的元素个数
        def max_array(num, number):
            # 要丢弃的元素数量
            discard = len(num) - number
            stack = []
            for ele in num:
                while stack and stack[-1] < ele and discard > 0:
                    stack.pop()
                    discard -= 1
                stack.append(ele)
            while discard:
                stack.pop()
                discard -= 1
            return stack

        def merge(num1, num2):
            res = []
            while num1 or num2:
                if num2 > num1:
                    num1, num2 = num2, num1
                res.append(num1.pop(0))
            return res

        res = []
        len_1, len_2 = len(nums1), len(nums2)
        for i in range(len_1 + 1):
            j = k - i
            if 0 <= j <= len_2:
                temp = merge(max_array(nums1, i), max_array(nums2, j))
                if not res:
                    res = temp
                    continue
                for m in range(k):
                    if temp[m] > res[m]:
                        res = temp
                        break
                    elif temp[m] < res[m]:
                        break
        return res


if __name__ == '__main__':
    s = Solution()
    num1 = [6,7]
    num2 = [6,0,4]
    k = 5
    print(s.maxNumber(num1, num2, k))
