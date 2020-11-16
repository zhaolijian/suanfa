# -*- coding:utf-8 -*-
# 方法一
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         ss = ""
#         for j in range(len(s)):
#             if s[j] == ' ':
#                 ss += "%20"
#             else:
#                 ss += s[j]
#         return ss


# 方法2
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         return s.replace(" ", "%20")


# 方法3
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return "%20".join(s.split())


if __name__ == '__main__':
    s = Solution()
    string = "we are  lucky"
    print(s.replaceSpace(string))
