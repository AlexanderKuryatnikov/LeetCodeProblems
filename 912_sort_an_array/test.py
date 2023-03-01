from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: reversed array': [
        [5, 2, 3, 1],
        [1, 2, 3, 5]
    ],
    '2: repeating numbers': [
        [5, 1, 1, 2, 0, 0],
        [0, 0, 1, 1, 2, 5]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.sortArray(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
