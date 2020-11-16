# class Solution:
#     def InversePairs(self, data):
#         if len(data) <= 1:
#             return 0
#         sum = 0
#         for index in range(len(data) - 1, -1, -1):
#             for i in range(index):
#                 if data[i] > data[index]:
#                     sum += 1
#         return sum


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        self.reverseNumber(data)
        return self.count % 1000000007

    def reverseNumber(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        temp = []
        left = self.reverseNumber(data[:mid])
        right = self.reverseNumber(data[mid:])
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                temp.append(left[l])
                l += 1
            else:
                temp.append(right[r])
                r += 1
                self.count += (len(left) - l)
        temp += right[r:]
        temp += left[l:]
        return temp


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    print(s.InversePairs(l))


