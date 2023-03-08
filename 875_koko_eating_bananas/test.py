from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [3, 6, 7, 11],
        8,
        4
    ],
    '2: leetcode example 2': [
        [30, 11, 23, 4, 20],
        5,
        30
    ],
    '3: leetcode example 3': [
        [30, 11, 23, 4, 20],
        6,
        23
    ],
    '4: one pile with a lot of time': [
        [20],
        10,
        2
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minEatingSpeed(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
