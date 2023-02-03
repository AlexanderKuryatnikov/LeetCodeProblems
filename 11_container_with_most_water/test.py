from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example': [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        49
    ],
    '2: reversed leetcode example': [
        [7, 3, 8, 4, 5, 2, 6, 8, 1],
        49
    ],
    '3: two lines': [
        [1, 1],
        1
    ],
    '4: no lines': [
        [0, 0, 0],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.maxArea(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
