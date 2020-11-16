# 给定一个数组，找出数组的最长连续子序列。例：3,3,4,7,5,6,8
# 最长的连续子序列（这里的连续是说连续整数，整个子序列是连续整数）应该是(3,4,5,6)，
# 需要返回它们的下标(1,2,4,5)。如果存在多种答案，只需给出任意一组下标。
# 方法1 哈希表
class Solution:
    def solution(self, a):
        n = len(a)
        # 记录前面的连续数字位置
        pre = [0] * n
        # 记录数字和以它为结尾的最长连续子序列长度
        dic = {a[0]: 1}
        # 记录数字及对应的索引位置
        idx = {a[0]: 0}
        MAX_len, last = 0, 0
        pre[0] = -1
        for i in range(1, n):
            if a[i] not in dic:
                if a[i] - 1 not in dic:
                    dic[a[i]] = 1
                    pre[i] = -1
                else:
                    dic[a[i]] = dic[a[i] - 1] + 1
                    pre[i] = idx[a[i] - 1]
                idx[a[i]] = i
            else:
                if a[i] - 1 not in dic:
                    continue
                elif dic[a[i]] < dic[a[i] - 1] + 1:
                    dic[a[i]] = dic[a[i] - 1] + 1
                    pre[i] = idx[a[i] - 1]
                    idx[a[i]] = i
            if dic[a[i]] > MAX_len:
                MAX_len = dic[a[i]]
                last = i
        rtn = []
        res = []
        while last != -1:
            rtn.append(last)
            res.append(a[last])
            last = pre[last]
        print("val:", res[::-1])
        print("index:", rtn[::-1])

# 方法2 双层遍历 复杂度O(n^2)
# class Solution:
#     def solution(self, array):
#         length = len(array)
#         res = []
#         for i in range(length):
#             temp = [i]
#             res = temp if len(temp) > len(res) else res
#             for j in range(i + 1, length):
#                 if array[j] == array[temp[-1]] + 1:
#                     temp.append(j)
#                     res = temp if len(temp) > len(res) else res
#         return res


if __name__ == '__main__':
    s = Solution()
    array = list(map(int, input().split()))
    print(s.solution(array))