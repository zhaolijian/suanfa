# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。


# 方法1 原地修改双指针，奇数位置一个指针，偶数位置一个指针，从前往后遍历，选出各自不符合的进行交换
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        j = 1
        for i in range(0, length, 2):
            # 偶数的位置如果是个奇数
            if A[i] % 2:
                # 找到偶数和它交换
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


# 方法2 遍历两边数组，第一次将偶数放到偶数位置，第二次将奇数放到奇数位置。
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i = 0
        for ele in A:
            if ele % 2 == 0:
                res[i] = ele
                i += 2
        j = 1
        for ele in A:
            if ele % 2:
                res[j] = ele
                j += 2
        return res