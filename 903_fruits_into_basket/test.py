from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: one tree': [
        [1],
        1
    ],
    '2: two tree types': [
        [2, 1, 2, 2, 2, 1, 1, 1, 2, 1],
        10
    ],
    '3: more than two tree types 1': [
        [5, 1, 2, 3, 2, 2],
        4
    ],
    '4: more than two tree types 2': [
        [1, 2, 3, 4, 5, 6, 7, 8],
        2
    ],
    '5: more than two tree types 2': [
        [1, 1, 2, 3, 1, 4, 1, 4, 1, 4, 5],
        6
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.totalFruit(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
