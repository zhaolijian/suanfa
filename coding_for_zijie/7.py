# 给定一个数组，找出数组的最长连续子序列。例：3,3,4,7,5,6,8
# 最长的连续子序列（这里的连续是说连续整数，整个子序列是连续整数）应该是(3,4,5,6)，
# 返回最长的长度
class Solution:
    def solution(self, array):
        length = len(array)
        if length <= 1:
            return length
        res = 1
        set_array = {array[0]: 1}
        for i in range(1, length):
            if array[i] not in set_array.keys():
                if array[i] - 1 in set_array.keys():
                    set_array[array[i]] = set_array[array[i] - 1] + 1
                else:
                    set_array[array[i]] = 1
            else:
                if array[i] - 1 not in set_array.keys():
                    continue
                elif set_array[array[i]] < set_array[array[i] - 1] + 1:
                    set_array[array[i]] = set_array[array[i] - 1] + 1
            res = max(res, set_array[array[i]])
        return res


if __name__ == '__main__':
    s = Solution()
    array = list(map(int, input().split()))
    print(s.solution(array))