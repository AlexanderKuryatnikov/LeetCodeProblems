class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-':
            x = '-' + x[:-1]
        x = int(x)
        if -pow(2, 31) < -x < pow(2, 31) - 1:
            return x
        return 0
