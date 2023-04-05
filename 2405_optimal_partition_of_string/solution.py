class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        substring = set()

        for char in s:
            if char in substring:
                substring = {char}
                result += 1
            else:
                substring.add(char)

        return result
