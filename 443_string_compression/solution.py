from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        p_original = 0
        p_compressed = 0
        while p_original < len(chars):
            current_char = chars[p_original]

            repeats = 0
            while (p_original < len(chars)
                   and current_char == chars[p_original]):
                p_original += 1
                repeats += 1

            chars[p_compressed] = current_char
            p_compressed += 1
            if repeats == 1:
                continue

            for num in str(repeats):
                chars[p_compressed] = num
                p_compressed += 1

        return p_compressed
