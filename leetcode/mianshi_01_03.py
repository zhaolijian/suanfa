# url化
# 方法1
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        array = list(S)
        for i in range(length):
            if array[i] == " ":
                array[i] = "%20"
        return ''.join(array[: length])


# 方法2
# class Solution:
#     def replaceSpaces(self, S: str, length: int) -> str:
#         return "%20".join(S[:length].split(" "))


# 方法3
# class Solution:
#     def replaceSpaces(self, S: str, length: int) -> str:
#         return S[:length].replace(" ", "%20")


if __name__ == '__main__':
    s = Solution()
    S = "     "
    length = 5
    print(s.replaceSpaces(S, length))