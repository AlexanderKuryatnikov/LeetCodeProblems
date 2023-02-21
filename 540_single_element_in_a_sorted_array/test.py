from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: target in the middle 1': [
        [1, 1, 2, 3, 3, 4, 4, 8, 8],
        2
    ],
    '2: target in the middle 2': [
        [3, 3, 7, 7, 10, 11, 11],
        10
    ],
    '3: target in the left': [
        [1, 2, 2],
        1
    ],
    '4: target in the right': [
        [1, 1, 2, 2, 3],
        3
    ],
    '5: one element': [
        [13],
        13
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.singleNonDuplicate(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
