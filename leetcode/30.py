# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。


# 方法1 哈希表
from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        c_words = Counter(words)
        word_length = len(words[0])
        length = word_length * len(words)
        res = []
        for i in range(len(s) - length + 1):
            c_s = defaultdict(int)
            for j in range(i, i + length, word_length):
                c_s[s[j: j + word_length]] += 1
            if c_words == c_s:
                res.append(i)
        return res


# 方法2 哈希表+滑动窗口。不需要每一个位置创建一个哈希表，通过滑动的方式增加减少单词数即可
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        c_words = Counter(words)
        len_word = len(words[0])
        len_words = len_word * len(words)
        len_s = len(s)
        if len_words > len_s:
            return []
        res = []
        for i in range(len_word):
            c_s = Counter()
            left, right = i, i + len_words - 1
            for i in range(left, right + 1, len_word):
                c_s[s[i: i + len_word]] += 1
            while right < len_s:
                if c_s == c_words:
                    res.append(left)
                c_s[s[left: left + len_word]] -= 1
                if c_s[s[left: left + len_word]] == 0:
                    c_s.pop(s[left: left + len_word])
                left += len_word
                c_s[s[right + 1: right + len_word + 1]] += 1
                right += len_word
        return res


# 方法3 哈希表+滑动窗口（与上面思路不一样）
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    # 当前遍历单词出现次数大于words中该单词出现次数，则左指针右移
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res

if __name__ == '__main__':
    s = Solution()
    ss = "barfoothefoobarman"
    words = ["foo","bar"]
    print(s.findSubstring(ss, words))