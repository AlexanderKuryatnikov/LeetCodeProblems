from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: interval exists': [
        [5, 7, 7, 8, 8, 10],
        8,
        [3, 4]
    ],
    '2: no target': [
        [5, 7, 7, 8, 8, 10],
        6,
        [-1, -1]
    ],
    '3: empty list': [
        [],
        0,
        [-1, -1]
    ],
    '4: single element is target': [
        [1],
        1,
        [0, 0]
    ],
    '5: list of targets': [
        [1, 1, 1, 1],
        1,
        [0, 3]
    ],
    '6: target greater': [
        [2, 2],
        3,
        [-1, -1]
    ],
    '7: target lesser': [
        [2, 2],
        1,
        [-1, -1]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.searchRange(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
