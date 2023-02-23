from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        2,
        0,
        [1, 2, 3],
        [0, 1, 1],
        4
    ],
    '2: leetcode example 2': [
        3,
        0,
        [1, 2, 3],
        [0, 1, 2],
        6
    ],
    '3: no funds': [
        4,
        0,
        [5, 3, 6],
        [1, 1, 1],
        0
    ],
    '4: one project fundable': [
        10,
        5,
        [10, 1, 20],
        [10, 4, 20],
        6
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.findMaximizedCapital(
            values[0],
            values[1],
            values[2],
            values[3]
        )
        assert values[4] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
