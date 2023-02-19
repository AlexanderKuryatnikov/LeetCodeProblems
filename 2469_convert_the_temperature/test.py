from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        36.5,
        [309.65, 97.7]
    ],
    '2: leetcode example 2': [
        122.11,
        [395.26, 251.798]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.convertTemperature(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
