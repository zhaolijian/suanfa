# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
# 剪枝+回溯
class Solution:
    def permutation(self, S: str):
        res = []
        length = len(S)
        S = sorted(S)
        # 记忆数组
        init = [False for i in range(length)]
        # array前缀字符串
        def func(array):
            if length == len(array):
                res.append(array)
                return
            for i in range(length):
                if not init[i]:
                    # 如果当前字符和前一个字符一样,且前一个字符没有被访问过,则跳过.相同相邻字符只能顺序访问
                    if i > 0 and S[i - 1] == S[i] and not init[i - 1]:
                        continue
                    init[i] = True
                    func(array + S[i])
                    init[i] = False
        func("")
        return res


if __name__ == '__main__':
    s = Solution()
    S = "qqe"
    print(s.permutation(S))