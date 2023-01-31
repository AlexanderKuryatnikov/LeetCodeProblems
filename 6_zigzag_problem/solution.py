class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s_len = len(s)
        new_s = [' '] * s_len
        j = 0

        i = 0
        while i < s_len:
            new_s[j] = s[i]
            j += 1
            i += 2 * numRows - 2

        for row in range(1, numRows - 1):
            i = row
            while i < s_len:
                new_s[j] = s[i]
                j += 1
                try:
                    new_s[j] = s[i + 2 * (numRows - row - 1)]
                    j += 1
                except IndexError:
                    break
                i += 2 * numRows - 2

        i = numRows - 1
        while i < s_len:
            new_s[j] = s[i]
            j += 1
            i += 2 * numRows - 2

        return ''.join(new_s)
