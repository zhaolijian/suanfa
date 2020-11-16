# 方法1
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         ver1 = version1.split('.')
#         ver2 = version2.split('.')
#         length1 = len(ver1)
#         length2 = len(ver2)
#         length = max(length1, length2)
#         if length1 < length:
#             for i in range(length1, length):
#                 ver1.append('0')
#         if length2 < length:
#             for i in range(length2, length):
#                 ver2.append('0')
#         for i in range(length):
#             if int(ver1[i]) > int(ver2[i]):
#                 return 1
#             elif int(ver1[i]) < int(ver2[i]):
#                 return -1
#             if i == length-1:
#                 return 0
#             else:
#                 continue


# 方法2
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while v1 and v2:
            # pop函数为移除某个元素，并且返回它的值，默认移除最后一个元素。下面是移除第一个元素，并且返回第一个元素的值
            x = v1.pop(0)
            y = v2.pop(0)
            if x < y:
                return -1
            elif x > y:
                return 1
        if v1 and any(i > 0 for i in v1):
            return 1
        if v2 and any(i > 0 for i in v2):
            return -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion('1.0.1', '1.0.0'))
