# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
from heapq import heapify, heappop, heappush


# 方法1 最大堆，每次取次数最多的两个字母
class Solution:
    def reorganizeString(self, S: str) -> str:
        # 统计每个字母出现次数,如果最高次数大于(length + 1)//2,则返回“”
        # 否则,构建最大堆(即负数的最小堆),堆中的元素为(-1*次数,字母)
        init = [0] * 26
        length = len(S)
        for ele in S:
            init[ord(ele) - ord('a')] += 1
        for i in range(26):
            if init[i] > (length + 1) // 2:
                return ""
        array = []
        res = ""
        heapify(array)
        for i in range(26):
            if init[i]:
                heappush(array, (-init[i], chr(ord('a') + i)))
        while array:
            value1, ele1 = heappop(array)
            res += ele1
            # 因为value1是负的次数
            value1 += 1
            if array:
                value2, ele2 = heappop(array)
                res += ele2
                value2 += 1
                if value2 < 0:
                    heappush(array, (value2, ele2))
            if value1 < 0:
                heappush(array, (value1, ele1))
        return res


# 方法2
class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        init = [0] * 26
        for ele in S:
            init[ord(ele) - ord('a')] += 1
        for i in range(26):
            if init[i] > (length + 1) // 2:
                return ""
        res = [""] * length
        oddindex, evenindex = 1, 0
        for i in range(26):
            # 当前字母
            ele = chr(ord('a') + i)
            while 0 < init[i] <= length // 2 and oddindex < length:
                res[oddindex] = ele
                init[i] -= 1
                oddindex += 2
            # 如果length为奇数并且init[i]出现的次数为(length + 1)//2,则只能放在偶数位置
            # 另外一种情况就是奇数位置放完了，便从头开始放偶数位置
            while init[i] > 0:
                res[evenindex] = ele
                init[i] -= 1
                evenindex += 2
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    ss = "vvvlo"
    print(s.reorganizeString(ss))