# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。
# 有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。
# 给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。
# 注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
# 在结果列表中，选择字典序最小的名字作为真实名字。
from collections import defaultdict
class Solution:
    def trulyMostPopular(self, names, synonyms):
        def find(index):
            if parents[index] == index:
                return index
            parents[index] = find(parents[index])
            return parents[index]

        if not names:
            return []
        parents = {}
        for name in names:
            temp = name.split('(')
            parents[temp[0]] = temp[0]
        for temp in synonyms:
            i, j = temp.split(',')
            i, j = i[1:], j[:-1]
            if i not in parents:
                parents[i] = i
            if j not in parents:
                parents[j] = j
            if find(j) > find(i):
                parents[find(j)] = find(i)
            else:
                parents[find(i)] = find(j)
        res = defaultdict(int)
        for i, string in enumerate(names):
            name, last = string.split('(')
            percent = int(last[:-1])
            res[find(name)] += percent
        result = []
        for key in res.keys():
            result.append(key + '(' + str(res[key]) + str(')'))
        return result