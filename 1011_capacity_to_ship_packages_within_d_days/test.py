from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        5,
        15
    ],
    '2: leetcode example 2': [
        [3, 2, 2, 4, 1, 4],
        3,
        6
    ],
    '3: leetcode example 3': [
        [1, 2, 3, 1, 1],
        4,
        3
    ],
    '4: one weight': [
        [10],
        1,
        10
    ],
    '5: one day with miltiple weights': [
        [3, 4, 5, 6],
        1,
        18
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.shipWithinDays(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
