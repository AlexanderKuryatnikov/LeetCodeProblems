from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: no nines': [
        [1, 2, 3],
        [1, 2, 4]
    ],
    '2: nine in the end': [
        [4, 5, 9, 0, 9],
        [4, 5, 9, 1, 0]
    ],
    '3: all nines': [
        [9, 9, 9, 9],
        [1, 0, 0, 0, 0]
    ],
    '4: several nines in the end': [
        [8, 4, 3, 9, 9, 9],
        [8, 4, 4, 0, 0, 0]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.plusOne(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
