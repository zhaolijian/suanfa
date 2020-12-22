# 给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的元组 i, j, k 的数量。
# 由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。


from collections import Counter
class Solution:
    def threeSumMulti(self, A, target: int) -> int:
        c = Counter(A)
        key_list = list(c.keys())
        key_list.sort()
        res, length = 0, len(key_list)
        for i, ele in enumerate(key_list):
            left, right = i + 1, length - 1
            val = target - ele
            while left < right:
                if key_list[left] + key_list[right] == val:
                    res += c[ele] * c[key_list[left]] * c[key_list[right]]
                    left += 1
                    right -= 1
                elif key_list[left] + key_list[right] > val:
                    right -= 1
                else:
                    left += 1
            # 只用一个数
            if 3 * ele == target and c[ele] >= 3:
                temp = 1
                number = c[ele]
                for i in range(3):
                    temp *= number
                    number -= 1
                temp //= 6
                res += temp
            # 只用当前遍历的两个数+另外一个(当前一个+两外两个和该情况重复)
            elif c[ele] >= 2:
                rest = target - 2 * ele
                if rest != ele and rest in c.keys():
                    temp = c[ele] * (c[ele] - 1) // 2
                    res += temp * c[rest]
        return res % (pow(10, 9) + 7)


if __name__ == '__main__':
    s = Solution()
    A = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    print(s.threeSumMulti(A, target))