class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        length = len(nums1) + len(nums2)
        sign = True
        if length % 2 == 1:
            sign = False
        return self.findMiddle(nums1, nums2, length, sign)


    def findMiddle(self, l1, l2, length, sign):
        # 如果sign为True,则找中间两个数的平均数
        # 如果sign为false,则找中间数
        # 使用归并排序
        l, r = 0, 0
        # 记录总位置
        temp = 0
        val = float('inf')
        res = []
        while l < len(l1) and r < len(l2):
            if l1[l] <= l2[r]:
                temp += 1
                val = l1[l]
                l += 1
            else:
                temp += 1
                val = l2[r]
                r += 1
            if sign and temp == (length - 1) // 2 + 1 or temp == (length - 1) // 2 + 2:
                res.append(val)
                if len(res) == 2:
                    return float(sum(res)) / 2
            elif not sign and temp == (length - 1) // 2 + 1:
                return val
        if l1[l:]:
            if sign:
                if res:
                    return float(res[0] + l1[l]) / 2
                else:
                    return float(l1[length // 2 - len(l2) - 1] + l1[length // 2 - len(l2)]) / 2
            else:
                if l2:
                    return l1[length // 2 - len(l2)]
                else:
                    return l1[len(l1) // 2]
        if l2[r:]:
            if sign:
                if res:
                    return float(res[0] + l2[r]) / 2
                else:
                    return float(l2[length // 2 - len(l1) - 1] + l2[length // 2 - len(l1)]) / 2
            # 奇数
            else:
                if l1:
                    return l2[length // 2 - len(l1)]
                else:
                    return l2[len(l2) // 2]


if __name__ == '__main__':
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    s = Solution()
    print(s.findMedianSortedArrays(num1, num2))