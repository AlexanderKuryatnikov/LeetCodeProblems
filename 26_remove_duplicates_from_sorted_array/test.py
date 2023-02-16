from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: no duplicates': [
        [1, 2, 3, 4, 5, 6],
        6,
        [1, 2, 3, 4, 5, 6]
    ],
    '2: several duplicates': [
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        5,
        [0, 1, 2, 3, 4]
    ],
    '3: one element': [
        [10],
        1,
        [10]
    ],
    '4: one duplicated element': [
        [5, 5, 5, 5],
        1,
        [5]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.removeDuplicates(values[0])
        assert values[2] == values[0][:result], (
            f'Test {test}. Your result {values[0][:result]}'
        )
        print(f'Test {test}... OK')
