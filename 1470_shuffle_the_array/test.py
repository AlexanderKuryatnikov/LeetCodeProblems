from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: n = 1': [
        [1, 2],
        1,
        [1, 2]
    ],
    '2: n is odd': [
        [1, 2, 3, 4, 5, 6],
        3,
        [1, 4, 2, 5, 3, 6],
    ],
    '3: n is even': [
        [1, 2, 3, 4, 5, 6, 7, 8],
        4,
        [1, 5, 2, 6, 3, 7, 4, 8]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.shuffle(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
