class Solution:
    def __init__(self):
        self.number = 0

    def validPalindrome(self, s: str) -> bool:
        def func(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if self.number < 1:
                        self.number += 1
                        return func(s, l + 1, r) or func(s, l, r - 1)
                    else:
                        return False
            return True

        return func(s, 0, len(s) - 1)