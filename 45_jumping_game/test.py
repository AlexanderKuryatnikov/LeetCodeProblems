from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [2, 3, 1, 1, 4],
        2
    ],
    '2: leetcode example 2': [
        [2, 3, 0, 1, 4],
        2
    ],
    '3: no jumps required': [
        [3],
        0
    ],
    '4: unjumpable spaces': [
        [2, 0, 4, 1, 0, 2, 0, 1],
        3
    ],
    '5: single jump required': [
        [9, 8, 9, 9, 9],
        1
    ],
    '6: best next jump is closest': [
        [4, 4, 1, 1, 1, 1],
        2
    ],
    '9: best next jump is furthest': [
        [4, 1, 1, 1, 1, 1],
        2
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.jump(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
