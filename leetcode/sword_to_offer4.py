# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


# 方法1 调用现成函数
# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         return s.replace(" ", "%20")


# 方法2
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        for ele in s:
            if ele == " ":
                res += "%20"
            else:
                res += ele
        return res
j


if __name__ == '__main__':
    s = Solution()
    ss = "We are happy."
    print(s.replaceSpace(ss))