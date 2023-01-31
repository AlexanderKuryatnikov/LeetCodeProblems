class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for bracket in s:
            if bracket in brackets_dict.values():
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            elif brackets_dict[bracket] == stack[-1]:
                del stack[-1]
            else:
                return False

        if len(stack) == 0:
            return True
        return False
