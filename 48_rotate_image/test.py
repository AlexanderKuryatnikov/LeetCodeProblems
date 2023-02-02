from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: even order': [
        [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ],
        [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]]
    ],
    '2: odd order': [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    ],
    '4: 1x1 matrix': [
        [[1]],
        [[1]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        matrix = values[0]
        solution.rotate(values[0])
        assert values[1] == matrix, f'Test {test}. Your result {matrix}'
        print(f'Test {test}... OK')
