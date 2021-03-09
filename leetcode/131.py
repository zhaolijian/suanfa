# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
# 方法1 dfs+dp
# 由于判断s[i,j]是否是回文串可能会重复多次（比如abcdabba，abba在后面，当从前往后遍历的时候，abba是否是回文串会判断多次），
# 所以使用dp把s[i,j]是否是回文串先获取到
class Solution:
    def partition(self, s: str):
        length = len(s)
        dp = [[True for i in range(length)] for j in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = dp[i + 1][j - 1] & (s[i] == s[j])
        res = []

        # 当前已经获取到的回文字符串数组作为参数
        # def dfs(already, index):
        #     if index == length:
        #         res.append(already)
        #         return
        #     for i in range(index, length):
        #         if dp[index][i]:
        #             dfs(already + [s[index: i + 1]], i + 1)
        # dfs([], 0)

        # 当前已经获取到的回文字符串数组放在外面
        cur = []
        def dfs(index):
            if index == length:
                # 不能使用cur，而应该使用cur[:]，cur[:]表示将当前cur数组拷贝一份，而使用cur的话，相当于记录cur指针，cur不断变化，最后返回一个[[],[]...]
                res.append(cur[:])
                return
            for i in range(index, length):
                if dp[index][i]:
                    cur.append(s[index: i + 1])
                    dfs(i + 1)
                    cur.pop()
        dfs(0)
        return res


class Solution:
    def partition(self, s: str):
        def findSubStr(already, next_index):
            nonlocal length
            if next_index == length:
                res.append(already)
                return
            # 长度为1的奇数回文串
            findSubStr(already+[s[next_index]], next_index + 1)
            rest_length = length - next_index
            # 奇数回文串
            # 以回文串一半的长度遍历（这也可以对子串最右侧索引遍历，表达式写起来会简单很多）
            for half_len in range(1, (rest_length - 1) // 2 + 1):
                if s[next_index: next_index + half_len] == s[next_index + half_len + 1: next_index + half_len * 2 + 1][::-1]:
                    findSubStr(already+[s[next_index: next_index + half_len * 2 + 1]], next_index + half_len * 2 + 1)
            # 偶数回文串
            for half_len in range(1, rest_length // 2 + 1):
                if s[next_index: next_index + half_len] == s[next_index + half_len: next_index + half_len * 2][::-1]:
                    findSubStr(already+[s[next_index: next_index + half_len * 2]], next_index + half_len * 2)

        res = []
        length = len(s)
        findSubStr([], 0)
        return res