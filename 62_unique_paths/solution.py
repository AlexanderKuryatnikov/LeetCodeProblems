class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_num = 1
        if n > m:
            n, m = m, n
        for i in range(1, n):
            paths_num = paths_num * (m - 1 + i) // i
        return paths_num
