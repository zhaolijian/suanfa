# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


# 自定义排序字符串之使用快速排序
class Solution:
    def minNumber(self, nums) -> str:
        def quick_sort(l, r):
            if l >= r:
                return
            left, right = l, r
            key = strs[l]
            while left < right:
                while left < right and key + strs[right] <= strs[right] + key:
                    right -= 1
                strs[left] = strs[right]
                while left < right and strs[left] + key <= key + strs[left]:
                    left += 1
                strs[right] = strs[left]
            strs[left] = key
            quick_sort(l, left - 1)
            quick_sort(left + 1, r)

        strs = map(str, nums)
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


# 自定义排序字符串之使用内置函数
# from functools import cmp_to_key
# class Solution:
#     def minNumber(self, nums) -> str:
#         def cmp(x, y):
#             if x + y > y + x:
#                 return 1
#             elif x + y < y + x:
#                 return -1
#             else:
#                 return 0
#         strs = map(str, nums)
#         result = sorted(strs, key=cmp_to_key(cmp))
#         return "".join(result)


if __name__ == '__main__':
    s = Solution()
    nums = [3,30,34,5,9]
    print(s.minNumber(nums))