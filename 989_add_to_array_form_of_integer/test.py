from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 0, 0],
        34,
        [1, 2, 3, 4]
    ],
    '2: leetcode example 1': [
        [2, 7, 4],
        181,
        [4, 5, 5]
    ],
    '3: leetcode example 3': [
        [2, 1, 5],
        806,
        [1, 0, 2, 1]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.addToArrayForm(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
