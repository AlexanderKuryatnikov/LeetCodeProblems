from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ],
        3,
        True
    ],
    '2: leetcode example 2': [
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ],
        13,
        False
    ],
    '3: one row 1': [
        [[1, 3, 5, 7, 9, 10]],
        5,
        True
    ],
    '4: one row 2': [
        [[1, 3, 5, 7, 9, 10]],
        9,
        True
    ],
    '5: one row 3': [
        [[1, 3, 5, 7, 9, 10]],
        2,
        False
    ],
    '6: one row 4': [
        [[1, 3, 5, 7, 9, 10]],
        8,
        False
    ],
    '7: one col 1': [
        [[1], [3], [3], [5], [7], [9], [11]],
        1,
        True
    ],
    '8: one col 2': [
        [[1], [3], [3], [5], [7], [9], [11]],
        5,
        True
    ],
    '9: one col 3': [
        [[1], [3], [3], [5], [7], [9], [11]],
        4,
        False
    ],
    '10: one col 4': [
        [[1], [3], [3], [5], [7], [9], [11]],
        10,
        False
    ],
    '11: 1x1 matrix with target': [
        [[1]],
        1,
        True
    ],
    '12: 1x1 matrix without target': [
        [[1]],
        0,
        False
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.searchMatrix(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
