# 给一个n个数字（1e5）。求有多少个区间出现最多的数字的次数大于等于m。
# 输入：
# 5 2
# 1 2 1 2 5
# 输出：
# 5
# 解释：区间[1,3][1,4][1,5][2,4][2,5]五个区间中最多的数字大于2。
# 注区间中的值表示第几个数，如[1,3]表示数组[1,2,1]，有两个1，大于等于2
class Solution:
    def func(self, a, m):
        pt = -1
        ans = 0
        # 值对应的位置集合
        pos = [[] for i in range(len(a) + 111)]
        # 每一次遍历统计到该遍历值为止的区间数
        for i in range(len(a)):
            v = a[i]
            pos[v].append(i)
            if len(pos[v]) >= m:
                pre_m = pos[v][-m]
                pt = max(pt, pre_m)
            ans += pt + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    while True:
        iline = input()
        if not iline:
            break
        n, m = list(map(int, iline.strip().split()))
        a = list(map(int, input().strip().split()))
        print(s.func(a, m))