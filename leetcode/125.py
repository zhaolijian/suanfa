# 方法1： 不使用api
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         length = len(s)
#         start, end = 0, length - 1
#         while start < end:
#             if 'A' <= s[start] <= 'Z' or 'a' <= s[start] <= 'z':
#                 if 'A' <= s[end] <= 'Z' or 'a' <= s[end] <= 'z':
#                     if s[start].lower() == s[end].lower():
#                         start += 1
#                         end -= 1
#                     else:
#                         return False
#                 elif '0' <= s[end] <= '9':
#                     return False
#                 else:
#                     end -= 1
#             elif '0' <= s[start] <= '9':
#                 if '0' <= s[end] <= '9':
#                     if s[start] == s[end]:
#                         start += 1
#                         end -= 1
#                     else:
#                         return False
#                 elif 'A' <= s[end] <= 'Z' or 'a' <= s[end] <= 'z':
#                     return False
#                 else:
#                     end -= 1
#             else:
#                 start += 1
#         return True


# 方法2： 使用isalnum()api
#         isdigit()  是否全是数字
#         isalpha()  是否全是字母
#         isalnum()  是否全是字母或数字
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         array = [ele.lower() for ele in s if ele.isalnum()]
#         return array == array[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = [ele.lower() for ele in s if ele.isalnum()]
        start, end = 0, len(array) - 1
        while start < end:
            if array[start] != array[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    # ss = "`l;`` 1o1 ??;l`"
    ss = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(ss))