class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while (i + 1) ** 2 <= n:
            i += 1

        return i
