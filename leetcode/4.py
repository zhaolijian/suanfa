# 方法1
from heapq import heapify, heappush, heappop
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        global temp
        len_1, len_2 = len(nums1), len(nums2)
        sum_length = len_1 + len_2
        # 为true表示长度总和奇数,否则表示长度总和偶数
        flag = True if sum_length % 2 else False
        min_heap = nums1 + nums2
        heapify(min_heap)
        number = 0
        while number < sum_length // 2:
            temp = heappop(min_heap)
            number += 1
        if flag:
            return heappop(min_heap)
        else:
            return (heappop(min_heap) + temp) / 2


# 最小堆+最大堆
from heapq import heapify, heappush, heappop
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len_1, len_2 = len(nums1), len(nums2)
        sum_length = len_1 + len_2
        # 为true表示长度总和奇数,否则表示长度总和偶数
        flag = True if sum_length % 2 else False
        min_heap, max_heap = nums1 + nums2, []
        heapify(min_heap)
        heapify(max_heap)
        number = 0
        while number < sum_length // 2:
            temp = heappop(min_heap)
            heappush(max_heap, -temp)
            number += 1
        if flag:
            return heappop(min_heap)
        else:
            return (heappop(min_heap) - heappop(max_heap)) / 2


# 方法2 双指针
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        res = []
        left1, left2, len1, len2 = 0, 0, len(nums1), len(nums2)
        length = len1 + len2
        # true表示奇数,false表示偶数
        flag = True if length % 2 else False
        number = 0
        while left1 < len1 and left2 < len2:
            if nums1[left1] < nums2[left2]:
                val = nums1[left1]
                left1 += 1
            else:
                val = nums2[left2]
                left2 += 1
            if flag and number == length // 2:
                return val
            if not flag:
                if number == length // 2 - 1 or number == length // 2:
                    res.append(val)
                if len(res) == 2:
                    return sum(res) / 2
            number += 1
        if left1 < len1:
            if flag:
                return nums1[length // 2 - len2]
            else:
                if res:
                    return (res[0] + nums1[left1]) / 2
                else:
                    return (nums1[length // 2 - len2 - 1] + nums1[length // 2 - len2]) / 2
        if left2 < len2:
            if flag:
                return nums2[length // 2 - len1]
            else:
                if res:
                    return (res[0] + nums2[left2]) / 2
                else:
                    return (nums2[length // 2 - len1 - 1] + nums2[length // 2 - len1]) / 2


if __name__ == '__main__':
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    s = Solution()
    print(s.findMedianSortedArrays(num1, num2))