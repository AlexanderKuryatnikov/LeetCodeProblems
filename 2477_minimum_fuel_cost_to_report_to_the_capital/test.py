from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: no roads': [
        [],
        1,
        0
    ],
    '2: all reprs travel once': [
        [[0, 1], [0, 2], [0, 3]],
        5,
        3
    ],
    '3: long brunches': [
        [
            [3, 1], [3, 2], [1, 0],
            [0, 4], [0, 5], [4, 6]
        ],
        2,
        7
    ],
    '4: node degree > 1': [
        [
            [0, 1], [2, 1], [2, 6],
            [1, 3], [3, 4], [5, 4]
        ],
        3,
        7
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minimumFuelCost(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
