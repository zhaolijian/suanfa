class Solution:
    def numTrees(self, n: int) -> int:
        # 1: 1
        # 2: 2
        # 3: 5
        # 4: 14
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            init = [1, 1, 2]
            i = 3
            while i <= n:
                temp = 0
                for key in range(i):
                    temp += init[key] * init[i - key - 1]
                init.append(temp)
                i += 1
            return init[-1]


if __name__ == '__main__':
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        print(s.numTrees(n))