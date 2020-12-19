# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

#方法1 前缀和+哈希表
from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        res = 0
        array = [0]
        s = defaultdict(int)
        for ele in A:
            array.append(array[-1] + ele)
        for ele in array:
            res += s[ele - S]
            s[ele] += 1
        return res


#方法2 找出所有1的位置，满足中间有S个1的子数组左右扩展，左边满足条件的有m个，右边满足的有n个，则以当前位置为子数组起始位置的有m*n个满足的
class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        res = 0
        array = [-1]
        for i, ele in enumerate(A):
            if ele == 1:
                array.append(i)
        array.append(len(A))
        if S == 0:
            for i in range(len(array) - 1):
                temp = array[i + 1] - array[i] - 1
                res += (1 + temp) * temp // 2
        else:
            for i in range(1, len(array) - S):
                left = array[i] - array[i - 1]
                right = array[i + S] - array[i + S - 1]
                res += left * right
        return res


if __name__ == '__main__':
    s = Solution()
    A = [1,0,1,0,1]
    S = 2
    print(s.numSubarraysWithSum(A, S))