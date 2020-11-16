# class Solution:
#     def maxInWindows(self, num, size):
#         queue, res, i = [], [], 0
#         while size > 0 and i < len(num):
#             if len(queue) > 0 and i - size + 1 > queue[0]:
#                 queue.pop(0)
#             while len(queue) > 0 and num[queue[-1]] < num[i]:
#                 queue.pop(0)
#             queue.append(i)
#             if i >= size - 1:
#                 res.append(num[queue[0]])
#             i += 1
#         return res


# 双端队列
class Solution:
    def maxInWindows(self, num, size):
        if size < 1 or not num:
            return []
        if size == 1:
            return num
        # 滑动窗口中的元素下标所对应的值是一个降序排列
        queue = [0]
        # 存放窗口中数据量
        length = 1
        res = []
        for i in range(1, len(num)):
            if queue[0] < i - size + 1:
                queue.pop(0)
                length -= 1
            while length:
                if num[i] > num[queue[-1]]:
                    queue.pop(-1)
                    length -= 1
                else:
                    break
            queue.append(i)
            length += 1
            if i + 1 >= size:
                res.append(num[queue[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    size = int(input())
    print(s.maxInWindows(l, size))
