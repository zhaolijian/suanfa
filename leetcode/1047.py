# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

# 方法1 栈
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ele in S:
            if stack and stack[-1] == ele:
                stack.pop()
            else:
                stack.append(ele)
        return ''.join(stack)


# 方法2（复杂度太高，用栈更好）
class Solution:
    def removeDuplicates(self, S: str) -> str:
        new_str = ""
        # 是否修改
        flag = False
        while True:
            i = 0
            while i < len(S):
                if i + 1 < len(S) and S[i] == S[i + 1]:
                    i += 2
                    flag = True
                else:
                    new_str += S[i]
                    i += 1
            if not flag:
                break
            S = new_str
            new_str = ""
            flag = False
        return new_str


class Solution:
    def removeDuplicates(self, S: str) -> str:
        def func(S):
            # 处理后的字符串、初始字符串长度、索引、删除次数
            res, length, right, number = "", len(S), 0, 0
            while right < length:
                if right < length - 1 and S[right] == S[right + 1]:
                    number += 1
                    right += 2
                else:
                    res += S[right]
                    right += 1
            return res if number == 0 else func(res)
        return func(S)
