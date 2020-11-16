# 给一个有序数组，求每个数的平方的结果，不重复的有几个
# -5，-5，-1，0，1，1，1，1，2，5
# 这里平方数不重复的一共4个
# 怎么样用O(1)的空间复杂度实现
class Solution:
    def func(self, array):
        res = set()
        for ele in array:
            res.add(pow(ele, 2))
        return len(res)


if __name__ == '__main__':
    s = Solution()
    array = list(map(int, input().strip().split()))
    print(s.func(array))
