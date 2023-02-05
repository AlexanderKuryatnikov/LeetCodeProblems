from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_dict = self.create_dict(p)

        i = 0
        while i <= len(s) - len(p):
            if s[i] not in p_dict:
                i += 1
                continue

            left = i
            try:
                while s[i] in p_dict and i - left < len(p):
                    i += 1
                right = i
            except IndexError:
                right = len(s)
            if right - left < len(p):
                continue

            s_dict = self.create_dict(s[left:right])
            if p_dict == s_dict:
                result.append(left)

            try:
                while s[i] in p_dict:
                    self.add_char(s_dict, s[i])
                    i += 1
                    s_dict[s[left]] -= 1
                    left += 1
                    if p_dict == s_dict:
                        result.append(left)
            except IndexError:
                pass

        return result

    def create_dict(self, string: str) -> dict:
        string_dict = {}
        for char in string:
            self.add_char(string_dict, char)
        return string_dict

    def add_char(self, string_dict: dict, char: str) -> None:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1
