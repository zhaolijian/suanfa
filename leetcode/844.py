# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
# 注意：如果对空文本输入退格字符，文本继续为空。


# 方法1 栈
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def func(string):
            array = []
            for ele in string:
                if ele == "#":
                    if array:
                        array.pop()
                else:
                    array.append(ele)
            return "".join(array)
        return func(S) == func(T)


# 方法2 从后往前遍历
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        number_s, number_t = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    number_s += 1
                    i -= 1
                elif number_s > 0:
                    number_s -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    number_t += 1
                    j -= 1
                elif number_t > 0:
                    number_t -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            else:
                if i >= 0 or j >= 0:
                    return False
            i -= 1
            j -= 1
        return True