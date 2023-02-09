from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        self.recursion_add_parenthesis('', 0, 0, n, combinations)
        return combinations

    def recursion_add_parenthesis(
            self,
            written_parantheses: str,
            left_added: int,
            right_added: int,
            n: int,
            combinations: List[str]
    ) -> str:
        if left_added == n and right_added == n:
            combinations.append(written_parantheses)
        if left_added < n:
            self.recursion_add_parenthesis(
                written_parantheses + '(',
                left_added + 1,
                right_added,
                n,
                combinations
            )
        if right_added < left_added:
            self.recursion_add_parenthesis(
                written_parantheses + ')',
                left_added,
                right_added + 1,
                n,
                combinations
            )
