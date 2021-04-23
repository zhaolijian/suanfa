# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，以下数列为等差数列:


class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        length = len(nums)
        if length < 3:
            return 0
        res = 0
        left = 0
        while left < length - 2:
            # 等差数列差值
            val = nums[left + 1] - nums[left]
            right = left + 1
            while right < length:
                if nums[right] - nums[right - 1] != val:
                    break
                right += 1
            if right - left >= 3:
                len_cur = right - left
                # (首项1+末项len_cur-2)*(项数len_cur-2)//2
                res += (len_cur - 1) * (len_cur - 2) // 2
                left = right - 1
            else:
                left += 1
        return res