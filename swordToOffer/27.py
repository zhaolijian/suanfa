# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]): # 依次固定了元素，其他的全排列（递归求解）
                res.add(ss[i] + j) # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
        return sorted(res)         # sorted()能对可迭代对象进行排序,结果返回一个新的list





if __name__ == '__main__':
    s = Solution()
    l = input()
    print(s.Permutation())