from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        12,
        5,
        17
    ],
    '2: leetcode example 2': [
        -10,
        4,
        -6
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.sum(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
