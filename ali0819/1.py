# class Solution:
#     def func(self, n, array):
#         res = [0] * n
#         res[0] = max(array)
#         res[-1] = min(array)
#         length = len(array)
#         for i in range(length):
#             val = 1
#             last_ou = array[i]
#             # 连续数为偶数
#             while i - val >= 0 and i + val - 1 <= length - 1:
#                 temp = min(last_ou, array[i - val], array[i + val - 1])
#                 last_ou = temp
#                 res[2 * val - 1] = max(res[2 * val - 1], temp)
#                 val += 1
#             val = 1
#             last_ji = array[i]
#             # 连续数为奇数
#             while i - val >= 0 and i + val <= length - 1:
#                 temp = min(last_ji, array[i - val], array[i + val])
#                 last_ji = temp
#                 res[2 * val] = max(res[2 * val], temp)
#                 val += 1
#         return res

class Solution:
    def func(self, n, array):
        res = [0] * n
        res[0] = max(array)
        res[-1] = min(array)
        length = len(array)
        for i in range(1, length):
            val = 1
            last_ou = array[i]
            # 连续数为偶数
            while i - val >= 0 and i + val - 1 <= length - 1:
                temp = min(last_ou, array[i - val], array[i + val - 1])
                last_ou = temp
                res[2 * val - 1] = max(res[2 * val - 1], temp)

                if i + val <= length - 1:
                    temp_ji = min(temp, array[i + val])
                    res[2 * val] = max(res[2 * val], temp_ji)
                val += 1
        return res
    # res = s.func(n, array)
    # print(' '.join(map(str, res)))

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    s = Solution()
    res = s.func(n, array)
    for i in range(len(res) - 1):
        print(res[i], end=' ')
    print(res[-1])