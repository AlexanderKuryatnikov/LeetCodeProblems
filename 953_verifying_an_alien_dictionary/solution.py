from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            for char in range(len(words[i])):
                try:
                    char1_position = order.index(words[i][char])
                    char2_position = order.index(words[i+1][char])
                    if char1_position > char2_position:
                        return False
                    if char1_position < char2_position:
                        break
                except IndexError:
                    return False
        return True
