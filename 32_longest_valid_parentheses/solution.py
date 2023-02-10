class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        max_len = 0

        while left <= right:
            if s[left] == '(':
                break
            left += 1
        while left <= right:
            if s[right] == ')':
                break
            right -= 1

        while left < right:

            current_len = 0
            opened_parentheses = 0
            starting_point = left
            while left <= right:
                if s[left] == '(':
                    opened_parentheses += 1
                    current_len += 1
                elif s[left] == ')' and opened_parentheses > 0:
                    opened_parentheses -= 1
                    current_len += 1
                else:
                    break
                left += 1

            if opened_parentheses > 0:
                left = starting_point
            if max_len < current_len and opened_parentheses == 0:
                max_len = current_len
            while left <= right:
                if s[left] == '(':
                    break
                left += 1

            current_len = 0
            opened_parentheses = 0
            starting_point = right
            while left <= right:
                if s[right] == ')':
                    opened_parentheses += 1
                    current_len += 1
                elif s[right] == '(' and opened_parentheses > 0:
                    opened_parentheses -= 1
                    current_len += 1
                else:
                    break
                right -= 1

            if opened_parentheses > 0:
                right = starting_point
            if max_len < current_len and opened_parentheses == 0:
                max_len = current_len
            while left < right:
                if s[right] == ')':
                    break
                right -= 1

        return max_len
