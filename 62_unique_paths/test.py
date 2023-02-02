from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: 3x7 grid': [3, 7, 28],
    '2: 3x2 grid': [3, 2, 3],
    '3: 1x1 grid': [1, 1, 1],
    '4: 1x7 grid': [1, 7, 1],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.uniquePaths(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
