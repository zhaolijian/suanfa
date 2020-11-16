# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         res = 0
#         if rows == 1:
#             for i in range(cols):
#                 temp = sum(map(int, list(str(i))))
#                 if threshold >= temp:
#                     res += 1
#                 else:
#                     break
#         elif cols == 1:
#             for i in range(rows):
#                 temp = sum(map(int, list(str(i))))
#                 if threshold >= temp:
#                     res += 1
#                 else:
#                     break
#         else:
#             for i in range(rows):
#                 for j in range(cols):
#                     temp = sum(map(int, list(str(i)))) + sum(map(int, list(str(j))))
#                     if threshold >= temp:
#                         res += 1
#         return res

class Solution:
    def movingCount(self, threshold, rows, cols):
        res = 0
        if rows == 1:
            for i in range(cols):
                if threshold >= sum(map(int, list(str(i)))):
                    res += 1
                else:
                    break
        elif cols == 1:
            for i in range(rows):
                if threshold >= sum(map(int, list(str(i)))):
                    res += 1
                else:
                    break
        else:
            for i in range(rows):
                for j in range(cols):
                    if threshold >= (sum(map(int, list(str(i)))) + sum(map(int, list(str(j))))):
                        res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(5, 10, 10))
