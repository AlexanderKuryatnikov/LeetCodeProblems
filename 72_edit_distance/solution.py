class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dist_table = []
        dist_table.append([i for i in range(n + 1)])
        for i in range(1, m + 1):
            dist_table.append([i])
            dist_table[i].extend([None] * n)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[j - 1] == word2[i - 1]:
                    dist_table[i][j] = dist_table[i - 1][j - 1]
                else:
                    dist_table[i][j] = (
                        1 + min(dist_table[i - 1][j - 1],
                                dist_table[i][j - 1],
                                dist_table[i - 1][j])
                    )

        return dist_table[-1][-1]
