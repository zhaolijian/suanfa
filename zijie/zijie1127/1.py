# a= [1,2,3,-1,4]，给定一个K值，比如K=8，返回连续子数组和>=K的最小子数组的长度，如果不存在则返回-1


class Solution:
    def func(self, array, K):
        length = len(array)
        # 开始索引
        index = 0
        # 累加值
        number = 0
        res = float('inf')
        for i in range(length):
            if number > 0:
                number += array[i]
            else:
                number = array[i]
                index = i
            # 累加值大于等于K,index右移找到最小满足的位置
            if number >= K:
                res = min(res, i - index + 1)
                while index < i:
                    number -= array[index]
                    index += 1
                    if number >= K:
                        res = min(res, i - index + 1)
                    else:
                        break
        return res if res != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    # array = [-5,1,-2,3,4,1,2,-1,3]
    # K=7
    array = [1,2,3,-1,4]
    K = 8
    print(s.func(array, K))