class Solution:
    def __init__(self):
        self.s = ''
        self.number = 0
        self.init = [[] for i in range(256)]

    # 返回对应char
    def FirstAppearingOnce(self):
        res = float('inf')
        for j in range(256):
            if len(self.init[j]) == 1 and self.init[j][0] < res:
                res = self.init[j][0]
        if res == float('inf'):
            return '#'
        return self.s[res]

    def Insert(self, char):
        self.s += char
        self.init[ord(char)].append(self.number)
        self.number += 1


if __name__ == '__main__':
    print(ord('a'))