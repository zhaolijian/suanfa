# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
# 1 <= k < s.length <= 10000

# 方法1 时间复杂度O(n), 空间复杂度O(n)，由于python字符串不能原地操作，所以空间复杂度较高
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        length = len(s)
        res = ""
        for i in range(n, n + length):
            res += s[i % length]
        return res


# 如果允许字符串原地操作的话
# 具体步骤为：
# 反转区间为前n的子串
# 反转区间为n到末尾的子串
# 反转整个字符串
# 「最后就可以得到左旋n的目的，而不用定义新的字符串，完全在本串上操作。」
#
# 例如 ：示例1中 输入：字符串abcdefg，n=2
#
# 反转区间为前n的子串 ：bacdefg
# 反转区间为n到末尾的子串：bagfedc
# 反转整个字符串：cdefgab
# 最终得到左旋2个单元的字符串：cdefgab