# 把数组排成最小的数


# class Solution:
#     def PrintMinNumber(self, numbers):
#         if len(numbers) == 0:
#             return ''
#         numbers.sort()
#         numbers = list(map(str, numbers))
#         for i in range(len(numbers)-1):
#             a = numbers[i] + numbers[i+1]
#             b = numbers[i+1] + numbers[i]
#             temp = a if int(a) <= int(b) else b
#             numbers[i+1] = temp
#         return numbers[-1]


# 思路二：创建另一个数组，每一个元素的长度都一样，不足的用第一个元素补齐，然后对新创建的数组排序，并用相同的顺序调整原数组
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ''
        max_number = max(numbers)
        length = len(str(max_number))
        str_numbers = list(map(str, numbers))
        for i in range(len(str_numbers)):
            temp = len(str_numbers[i])
            str_numbers[i] = str_numbers[i] + str_numbers[i][-1] * (length - temp)
        for j in range(len(str_numbers)):
            for k in range(len(str_numbers) - 1):
                if int(str_numbers[k]) > int(str_numbers[k+1]):
                    str_numbers[k], str_numbers[k+1] = str_numbers[k+1], str_numbers[k]
                    numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
        res = ""
        for ele in numbers:
            res += str(ele)
        return res


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    print(s.PrintMinNumber(l))
