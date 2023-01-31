class Solution:
    def longestPalindrome(self, s: str) -> str:
        for sub_len in range(len(s), 0, -1):
            for i in range(0, len(s) - sub_len + 1):
                sub_s = s[i: sub_len + i]
                if sub_s == sub_s[::-1]:
                    return sub_s
