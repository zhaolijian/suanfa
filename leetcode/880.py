# 复杂度太高
# class Solution:
#     def decodeAtIndex(self, S: str, K: int) -> str:
#         # 已扩展字符串的当前长度
#         cur_length = 0
#         # 当前遍历到的S位置
#         index = 0
#         # S长度
#         length = len(S)
#         string = ''
#         while K > cur_length:
#             if index < length:
#                 # 如果当前遍历值是字母
#                 if S[index].isalpha():
#                     string += S[index]
#                     cur_length += 1
#                 else:
#                     number = int(S[index])
#                     string *= number
#                     cur_length *= number
#                 index += 1
#         if K > cur_length:
#             return None
#         else:
#             return string[K - 1]


# 逆推法
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # 扩展后字符串总长度
        size = 0
        for ele in S:
            if ele.isalpha():
                size += 1
            else:
                size *= int(ele)
        # 如果K值大于总长度，则说明越界
        if K > size:
            return None
        # 从后往前遍历字符串
        for j in range(len(S) - 1, -1, -1):
            K %= size
            if K == 0 and S[j].isalpha():
                return S[j]
            elif S[j].isdigit():
                size //= int(S[j])
            else:
                size -= 1


if __name__ == '__main__':
    s = Solution()
    ss = "ixm5xmgo78"
    K = 711
    print(s.decodeAtIndex(ss, K))