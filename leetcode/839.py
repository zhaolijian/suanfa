# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
# 形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？


# 并查集
class Solution:
    def numSimilarGroups(self, strs) -> int:
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parents[find(node1)] = find(node2)

        def isLike(word1, word2):
            len_word = len(word1)
            res = 0
            for i in range(len_word):
                if word1[i] != word2[i]:
                    res += 1
                if res > 2:
                    return False
            return True

        length = len(strs)
        parents = [i for i in range(length)]
        for i in range(length):
            for j in range(i + 1, length):
                if find(i) == find(j):
                    continue
                if isLike(strs[i], strs[j]):
                    union(i, j)
        return sum(1 for i in range(length) if parents[i] == i)


if __name__ == '__main__':
    s = Solution()
    strs = ["tars","rats","arts","star"]
    print(s.numSimilarGroups(strs))