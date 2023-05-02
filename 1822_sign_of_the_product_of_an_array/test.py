from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: product is positive': [
        [-1, -2, -3, -4, 3, 2, 1],
        1
    ],
    '2: product equals to zero': [
        [1, 5, 0, 2, -3],
        0
    ],
    '3: product is negative': [
        [-1, 1, -1, 1, -1],
        -1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.arraySign(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
