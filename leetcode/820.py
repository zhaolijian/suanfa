# 单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：
# words.length == indices.length
# 助记字符串 s 以 '#' 字符结尾
# 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等
# 给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。


# 方法1 set集合
class Solution:
    def minimumLengthEncoding(self, words) -> int:
        s = set(words)
        for word in words:
            for i in range(1, len(word)):
                s.discard(word[i:])
        return sum(len(ele) + 1 for ele in s)


# 方法2 字典树