class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        last_char = i

        try:
            while s[i] != ' ':
                i -= 1
            first_char = i
        except IndexError:
            first_char = -1

        return last_char - first_char
