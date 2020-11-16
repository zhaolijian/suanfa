# 计算右侧小于当前元素的个数 归并排序+索引数组
# 因为归并后的顺序会乱，每个数都可能不在原来的位置上了，统计右侧小于当前元素的个数没法统计，所以对索引数组进行归并排序操作
class Solution:
    def countSmaller(self, nums):
        def func(l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            func(l, mid)
            func(mid + 1, r)
            # temp中l到mid是左半有序,mid+1到r是右半有序
            for k in range(l, r + 1):
                temp[k] = indexs[k]
            left, right = l, mid + 1
            cur = l
            while left <= mid and right <= r:
                if nums[temp[left]] <= nums[temp[right]]:
                    indexs[cur] = temp[left]
                    # 这一手操作比较好，如果当nums[temp[left]]>nums[temp[right]]时，进行这样计算：res[temp[left]] += right - mid，
                    # 那么对于right>r情况，如果进行这样计算：res[temp[left]] += r - mid，则会重复计算一次。
                    res[temp[left]] += right - mid - 1
                    left += 1
                else:
                    indexs[cur] = temp[right]
                    right += 1
                cur += 1
            if left <= mid:
                indexs[cur: r + 1] = temp[left: mid + 1]
                for p in range(left, mid + 1):
                    res[temp[p]] += r - mid
            if right <= r:
                indexs[cur: r + 1] = temp[right: r + 1]

        length = len(nums)
        if length == 0:
            return []
        elif length == 1:
            return [0]
        # 用于临时将indexs的某个区间赋值给temp，存储上一次迭代值
        temp = [None for i in range(length)]
        # indexs保存每一次迭代排序好的结果
        indexs = [i for i in range(length)]
        res = [0 for i in range(length)]
        func(0, length - 1)
        return res



# 他人写的,同样的思路
# class Solution:
#     def countSmaller(self, nums):
#         size = len(nums)
#         if size == 0:
#             return []
#         if size == 1:
#             return [0]
#
#         temp = [None for _ in range(size)]
#         indexes = [i for i in range(size)]
#         res = [0 for _ in range(size)]
#
#         self.__helper(nums, 0, size - 1, temp, indexes, res)
#         return res
#
#     def __helper(self, nums, left, right, temp, indexes, res):
#         if left == right:
#             return
#         mid = left + (right - left) // 2
#
#         # 计算一下左边
#         self.__helper(nums, left, mid, temp, indexes, res)
#         # 计算一下右边
#         self.__helper(nums, mid + 1, right, temp, indexes, res)
#
#         if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
#             return
#         self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)
#
#     def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
#         # [left,mid] 前有序数组
#         # [mid+1,right] 后有序数组
#
#         # 先拷贝，再合并
#
#         for i in range(left, right + 1):
#             temp[i] = indexes[i]
#
#         l = left
#         r = mid + 1
#         for i in range(left, right + 1):
#             if l > mid:
#                 # l 用完，就拼命使用 r
#                 # [1,2,3,4] [5,6,7,8]
#                 indexes[i] = temp[r]
#                 r += 1
#             elif r > right:
#                 # r 用完，就拼命使用 l
#                 # [6,7,8,9] [1,2,3,4]
#                 indexes[i] = temp[l]
#                 l += 1
#                 # 注意：此时前面剩下的数，比后面所有的数都大
#                 res[indexes[i]] += (right - mid)
#             elif nums[temp[l]] <= nums[temp[r]]:
#                 # [3,5,7,9] [4,6,8,10]
#                 indexes[i] = temp[l]
#                 l += 1
#                 # 注意：
#                 res[indexes[i]] += (r - mid - 1)
#             else:
#                 assert nums[temp[l]] > nums[temp[r]]
#                 # 上面两种情况只在其中一种统计就可以了
#                 # [3,5,7,9] [4,6,8,10]
#                 indexes[i] = temp[r]
#                 r += 1


if __name__ == '__main__':
    s = Solution()
    nums = [5,2,6,1]
    print(s.countSmaller(nums))