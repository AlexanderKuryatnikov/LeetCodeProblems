from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example': [
        [[3, 0, 8, 4],
         [2, 4, 5, 7],
         [9, 2, 6, 3],
         [0, 3, 1, 0]],
        35
    ],
    '2: no increase': [
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.maxIncreaseKeepingSkyline(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
