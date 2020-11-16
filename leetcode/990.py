# 并查集
class Solution:
    def __init__(self):
        # 存储所有字母的父/根节点
        self.array = [i for i in range(26)]

    # 得到index的根节点
    def find(self, index):
        if self.array[index] == index:
            return index
        else:
            self.array[index] = self.find(self.array[index])
            return self.array[index]

    def equationsPossible(self, equations: List[str]) -> bool:
        for ele in equations:
            if ele[1] == '=':
                index1 = ord(ele[0]) - ord('a')
                index2 = ord(ele[3]) - ord('a')
                # index1的根节点接到index2的根节点下面，结果树中的所有节点相等
                self.array[self.find(index1)] = self.find(index2)
        for ele in equations:
            if ele[1] != '=':
                index1 = ord(ele[0]) - ord('a')
                index2 = ord(ele[3]) - ord('a')
                if self.find(index1) == self.find(index2):
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    equations = ["f==a","a==b","f!=e","a==c","b==e","c==f"]
    print(s.equationsPossible(equations))