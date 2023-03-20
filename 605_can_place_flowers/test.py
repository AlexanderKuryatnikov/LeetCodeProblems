from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: possible in the middle': [
        [1, 0, 0, 0, 1],
        1,
        True
    ],
    '2: not possible in the middle': [
        [1, 0, 0, 0, 1],
        2,
        False
    ],
    '3: possible in the beginning': [
        [0, 0, 0, 0, 1],
        2,
        True
    ],
    '4: not possible in the beginning': [
        [0, 0, 0, 0, 1],
        3,
        False
    ],
    '5: possible in the end': [
        [1, 0, 0],
        1,
        True
    ],
    '6: not possible in the end': [
        [1, 0, 0],
        2,
        False
    ],
    '7: no flowers to plant': [
        [1],
        0,
        True
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.canPlaceFlowers(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
