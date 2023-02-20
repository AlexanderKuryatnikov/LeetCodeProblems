class Solution:
    def isNumber(self, s: str) -> bool:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        signs = {'+', '-'}

        num_parts = s.lower().split('e')
        if len(num_parts) > 2:
            return False

        if len(num_parts) == 2:
            if num_parts[1] == '' or num_parts[1] in signs:
                return False
            start_index = 0
            if num_parts[1][0] in signs:
                start_index = 1
            for char in num_parts[1][start_index:]:
                if char not in digits:
                    return False

        if num_parts[0] == '' or num_parts[0] in signs:
            return False
        start_index = 0
        if num_parts[0][0] in signs:
            start_index = 1
        dot_used = False
        for char in num_parts[0][start_index:]:
            if char == '.' and dot_used:
                return False
            if char == '.':
                dot_used = True
                continue
            if char not in digits:
                return False
        if dot_used and len(num_parts[0][start_index:]) == 1:
            return False

        return True
