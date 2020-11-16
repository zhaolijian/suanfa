# 字符串压缩
class Solution:
    def compressString(self, S: str) -> str:
        length_pre = len(S)
        if length_pre <= 1:
            return S
        temp = ""
        temp_length = 1
        for i in range(1, length_pre):
            if S[i] == S[i - 1]:
                temp_length += 1
            else:
                temp += S[i - 1]
                temp += str(temp_length)
                temp_length = 1
        temp += S[-1]
        temp += str(temp_length)
        return temp if len(temp) < length_pre else S


if __name__ == '__main__':
    s = Solution()
    S = "aabcccccaa"
    print(s.compressString(S))