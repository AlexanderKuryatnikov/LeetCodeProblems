class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 0
        sub_char_set = {s[0]}

        sub_len = 1
        max_sub_len = 1

        while right < len(s) - 1:
            right += 1

            if s[right] in sub_char_set:
                while s[left] != s[right]:
                    sub_char_set.remove(s[left])
                    left += 1
                left += 1
            else:
                sub_char_set.add(s[right])

            sub_len = right - left + 1
            if sub_len > max_sub_len:
                max_sub_len = sub_len

        return max_sub_len
