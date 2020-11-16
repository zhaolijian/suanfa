# 给你两个有序整数数组nums1和nums2，请你将nums2合并到nums1中，使nums1成为一个有序数组。
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]


# 方法1
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        # nums1[:]一定要带"："，这样表示原nums1中的元素清空，如果不带的话说明定义一个和参数重名的局部变量，不再是原来的nums1了
        nums1[:] = []
        i, j = 0, 0
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1.append(temp[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1 += temp[i:]
        if j < n:
            nums1 += nums2[j:]


# 方法2 从后往前遍历，时间复杂度O(m + n), 空间复杂度O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l1, l2 = m - 1, n - 1
        number = m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[number] = nums2[l2]
                l2 -= 1
            else:
                nums1[number] = nums1[l1]
                l1 -= 1
            number -= 1
        if l2 >= 0:
            nums1[: number + 1] = nums2[:l2 + 1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(s.merge(nums1, m, nums2, n))
