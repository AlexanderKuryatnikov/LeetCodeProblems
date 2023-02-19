from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 1],
        [1, 2, 1, 1, 2, 1]
    ],
    '2: leetcode example 2': [
        [1, 3, 2, 1],
        [1, 3, 2, 1, 1, 3, 2, 1]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.getConcatenation(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
