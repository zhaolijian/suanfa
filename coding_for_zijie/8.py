# 给定一个数组，找出数组的最长连续子序列。例：3,3,4,7,5,6,8
# 最长的连续子序列（这里的连续是说连续整数，整个子序列是连续整数）应该是(3,4,5,6)，
# 返回最长的子序列值
class Solution:
    def solution(self, array):
        length = len(array)
        if length <= 1:
            return array
        init = {array[0]: 1}
        res = 1
        for i in range(1, length):
            if array[i] not in init:
                if array[i] - 1 in init:
                    init[array[i]] = init[array[i] - 1] + 1
                else:
                    init[array[i]] = 1
            else:
                if array[i] - 1 not in init:
                    continue
                else:
                    if init[array[i] - 1] + 1 > init[array[i]]:
                        init[array[i]] = init[array[i] - 1] + 1
            res = max(res, init[array[i]])
        result = []
        for key, val in init.items():
            if val == res:
                for i in range(res - 1, -1, -1):
                    result.append(key - i)
                break
        return result


if __name__ == '__main__':
    s = Solution()
    array = list(map(int, input().split()))
    print(s.solution(array))