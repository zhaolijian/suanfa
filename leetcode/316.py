# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。


from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        d = Counter(s)
        # 栈中有的元素
        set_array = set()
        for ele in s:
            if ele not in set_array:
                while stack and stack[-1] > ele and d[stack[-1]] > 1:
                    d[stack[-1]] -= 1
                    set_array.discard(stack.pop())
                set_array.add(ele)
                stack.append(ele)
            else:
                d[ele] -= 1
        return "".join(stack)


# 和上面思路一样
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        d = Counter(s)
        # 栈中有的元素
        set_array = set()
        for ele in s:
            if ele not in set_array:
                while stack and stack[-1] > ele and d[stack[-1]]:
                    set_array.discard(stack.pop())
                set_array.add(ele)
                stack.append(ele)
            # 每遍历到一个元素,该元素剩余数少1
            d[ele] -= 1
        return "".join(stack)



if __name__ == '__main__':
    s = Solution()
    ss = "bbcaac"
    print(s.removeDuplicateLetters(ss))