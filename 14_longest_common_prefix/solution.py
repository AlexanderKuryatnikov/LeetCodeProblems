from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            for i in range(len(prefix)):
                try:
                    if prefix[i] != word[i]:
                        prefix = word[:i]
                        break
                except IndexError:
                    prefix = word[:i]
                    break
            if not prefix:
                break
        return prefix


solution = Solution()
