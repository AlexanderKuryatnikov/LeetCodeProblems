from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: 1 row': [
        1,
        [[1]]
    ],
    '2: 2 rows': [
        2,
        [[1], [1, 1]]
    ],
    '3: 5 rows': [
        5,
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    ],
    '4: 6 rows': [
        6,
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ],
    ]
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.generate(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
