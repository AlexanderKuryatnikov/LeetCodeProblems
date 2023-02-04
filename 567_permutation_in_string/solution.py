class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = self.create_dict(s1)

        i = 0
        while i <= len(s2) - len(s1):
            if s2[i] not in s1_dict:
                i += 1
                continue

            left = i
            try:
                while s2[i] in s1_dict and i - left < len(s1):
                    i += 1
                right = i
            except IndexError:
                right = len(s2)
            if right - left < len(s1):
                continue

            s2_dict = self.create_dict(s2[left:right])
            if s1_dict == s2_dict:
                return True

            try:
                while s2[i] in s1_dict:
                    self.add_char(s2_dict, s2[i])
                    s2_dict[s2[left]] -= 1
                    if s1_dict == s2_dict:
                        return True
                    left += 1
                    i += 1
            except IndexError:
                return False

        return False

    def create_dict(self, s: str) -> dict:
        s_dict = {}
        for char in s:
            self.add_char(s_dict, char)
        return s_dict

    def add_char(self, s_dict: dict, char: str) -> None:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1
