# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。
# 如果存在则返回 true，不存在返回 false。

# 桶+map
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 所有桶中的元素索引差都在k的范围内,因为超出的都删除了
        bucket = {}
        bucket_size = t + 1
        for i, ele in enumerate(nums):
            # 桶号
            number = ele // bucket_size
            # 如果该桶中已经存在元素,则说明满足了值差绝对值小于等于t的条件,且满足索引差的绝对值小于等于t,返回true
            if number in bucket:
                return True
            # 如果该桶中没有元素,则放入
            bucket[number] = ele
            # 前一个桶中是否有满足条件的
            if number - 1 in bucket and abs(bucket[number - 1] - ele) <= t:
                return True
            # 后一个桶中是否有满足条件的
            if number + 1 in bucket and abs(bucket[number + 1] - ele) <= t:
                return True
            if i >= k:
                bucket.pop(nums[i - k] // bucket_size)
        return False