from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [2, 3, 5, 1, 3],
        3,
        [True, True, True, False, True]
    ],
    '2: leetcode example 2': [
        [4, 2, 1, 1, 2],
        1,
        [True, False, False, False, False]
    ],
    '3: leetcode example 3': [
        [12, 1, 12],
        10,
        [True, False, True]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.kidsWithCandies(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
