from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: target in array 1': [
        [1, 3, 5, 6],
        5,
        2
    ],
    '2: target in array 2': [
        [1, 3, 5, 6],
        1,
        0
    ],
    '3: target in array 3': [
        [1, 3, 5, 6],
        6,
        3
    ],
    '4: target in array 4': [
        [1, 3, 5, 6, 7],
        3,
        1
    ],
    '5: target in array 5': [
        [1, 3, 5, 6, 7],
        1,
        0
    ],
    '6: target in array 6': [
        [1, 3, 5, 6, 7],
        7,
        4
    ],
    '7: target not in array': [
        [1, 3, 5, 6],
        2,
        1
    ],
    '8: target not in array': [
        [1, 3, 5, 6, 8],
        7,
        4
    ],
    '9: target is right of array': [
        [1, 3, 5, 6],
        7,
        4
    ],
    '10: target is left of array': [
        [1, 3, 5, 6],
        -1,
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.searchInsert(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
