# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(map(int, str(n)))
        length = len(s)
        index = length-2
        while index >= 0:   # 寻找第一个比后面数字小的数字s[index]
            if s[index] < s[index+1]:
                break
            index -= 1
        if index < 0:   # 如果不存在，则元素按降序排列，返回-1
            return -1
        for j in range(length-1, index, -1):    # 寻找最后一个比s[index]大的数字s[j]
            if s[j] > s[index]:
                break
        s[index], s[j] = s[j], s[index] # s[j]与s[index]交换，并将s[index+1:]从小到大排序
        res = int(''.join(map(str, s[:index+1]+sorted(s[index+1:]))))
        return -1 if res > (1<<31)-1 else res   # 检查是否越界
    

if __name__ == '__main__':
    s = Solution()
    n = 12
    print(s.nextGreaterElement(n))