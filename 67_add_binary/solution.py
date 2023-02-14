class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        s_sum = ''
        next_place = 0

        for i in range(-1, -len(b) - 1, -1):
            place_sum = int(a[i]) + int(b[i]) + next_place
            if place_sum == 3:
                s_sum = '1' + s_sum
                next_place = 1
            elif place_sum == 2:
                s_sum = '0' + s_sum
                next_place = 1
            elif place_sum == 1:
                s_sum = '1' + s_sum
                next_place = 0
            else:
                s_sum = '0' + s_sum
                next_place = 0

        for i in range(-1 - len(b), -1 - len(a), -1):
            place_sum = int(a[i]) + next_place
            if place_sum == 2:
                s_sum = '0' + s_sum
                next_place = 1
            elif place_sum == 1:
                s_sum = '1' + s_sum
                next_place = 0
            else:
                s_sum = '0' + s_sum
                next_place = 0

        if next_place == 1:
            return '1' + s_sum
        return s_sum
