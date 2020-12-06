# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
class Solution:
    def reverseVowels(self, s: str) -> str:
        array = list(s)
        left, right = 0, len(s) - 1
        d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            while left < right and s[left] not in d:
                left += 1
            while left < right and s[right] not in d:
                right -= 1
            if left >= right:
                break
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        return "".join(array)