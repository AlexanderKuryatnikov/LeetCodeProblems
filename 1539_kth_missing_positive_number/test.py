from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: missing int inside arr': [
        [2, 3, 4, 7, 11],
        5,
        9
    ],
    '2: missing int after arr': [
        [1, 2, 3, 4],
        2,
        6
    ],
    '3: missing int before arr': [
        [5, 6, 7],
        3,
        3
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.findKthPositive(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
