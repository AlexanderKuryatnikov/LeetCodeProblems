from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 3],
        5,
        3
    ],
    '2: leetcode example 2': [
        [2],
        1,
        2
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minimumTime(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
