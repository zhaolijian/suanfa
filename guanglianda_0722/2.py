# 给定整数n，数组长度为n，元素为1-n，乱序，每次只能选择一个数放到前面，问最少多少次
# 输入第一行包含一个正整数n ，表示序列的长度。(1<=n<=100000)
# 接下来一行有n个正整数，表示序列中的n个元素，中间用空格隔开。(1<=a_i<=n)
# 方法：从后往前遍历，统计从n、n-1...，有多少元素的相对顺序是正确的。
# 如1 3 2 4 ，从后往前遍历，4和3的相对顺序是正确的，2出现在3后面，不正确，则结果为4-2=2
# 调整的话，直接把不正确的调前面即可。第一次调整：2 1 3 4 第二次调整 1 2 3 4
class Solution:
    def func(self, n, array):
        flag = sorted(array)
        count = 0
        j = n - 1
        for i in range(n - 1, -1, -1):
            if array[i] == flag[j]:
                count += 1
                j -= 1
        return n - count


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    array = list(map(int, input().strip().split()))
    print(s.func(n, array))