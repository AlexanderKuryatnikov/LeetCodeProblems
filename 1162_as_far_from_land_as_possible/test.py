from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ],
        2
    ],
    '2: leetcode example 2': [
        [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        4
    ],
    '3: 1x1 grid with 1': [
        [[1]],
        -1
    ],
    '4: 1x1 grid with 0': [
        [[0]],
        -1
    ],
    '5: single row with solution': [
        [[1, 0, 0, 0, 0, 0, 1]],
        3
    ],
    '6: single row without solution': [
        [[1, 1, 1, 1]],
        -1
    ],
    '7: single col with solution': [
        [[1], [0], [0], [0], [0], [1]],
        2
    ],
    '8: single col without solution': [
        [[0], [0], [0], [0], [0], [0]],
        -1
    ],
    '9: big grid 1': [
        [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        4
    ],
    '6: big grid 1': [
        [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ],
        2
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.maxDistance(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
