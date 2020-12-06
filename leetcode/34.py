# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗


# 二分法变形
# class Solution:
#     def searchRange(self, nums, target: int):
#         left = self.find(nums, target, True)
#         if left == len(nums) or nums[left] != target:
#             return [-1, -1]
#         else:
#             return [left, self.find(nums, target, False) - 1]
#
#     # 在nums找到target的最左侧/最右侧值
#     def find(self, nums, target, bool_val):
#         l, r = 0, len(nums)
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] > target or (bool_val and nums[mid] == target):
#                 r = mid
#             else:
#                 l = mid + 1
#         return l


# 先找到一个满足的，然后左右扩展找到边界
class Solution:
    def searchRange(self, nums, target: int):
        res = [-1, -1]
        length = len(nums)
        left, right = 0, length - 1
        flag = False
        while left <= right:
            if flag:
                break
            mid = (left + right) // 2
            if nums[mid] == target:
                l, r = mid, right
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        if nums[r] == target:
                            res[-1] = r
                            break
                        if m == r - 1 and nums[m] == target:
                            res[-1] = m
                            break
                        l = m
                    else:
                        r = m - 1
                l, r = left, mid
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        if r == m:
                            res[0] = m
                            flag = True
                            break
                        r = m
                    else:
                        l = m + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    target = 1
    print(s.searchRange(nums, target))