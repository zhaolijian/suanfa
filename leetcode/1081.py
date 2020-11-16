# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        s = set()
        stack = []
        for i in range(len(text)):
            if text[i] not in s:
                while stack and stack[-1] > text[i] and stack[-1] in text[i + 1:]:
                    s.remove(stack.pop())
                s.add(text[i])
                stack.append(text[i])
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    text = "cdadabcc"
    print(s.smallestSubsequence(text))