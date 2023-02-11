from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: continuous red nodes': [
        3,
        [[0, 1], [1, 2]],
        [],
        [0, 1, -1]
    ],
    '2: altering continuous nodes': [
        3,
        [[0, 1]],
        [[2, 1]],
        [0, 1, -1]
    ],
    '3: node through cycle': [
        5,
        [[0, 1], [1, 2], [2, 3], [3, 4]],
        [[1, 2], [2, 3], [3, 1]],
        [0, 1, 2, 3, 7]
    ],
    '4: paralel nodes': [
        3,
        [[0, 1], [0, 2]],
        [[1, 0]],
        [0, 1, 1]
    ],
    '5:': [
        6,
        [[4, 1], [3, 5], [5, 2], [1, 4],
         [4, 2], [0, 0], [2, 0], [1, 1]],
        [[5, 5], [5, 0], [4, 4], [0, 3], [1, 0]],
        [0, -1, 4, 1, -1, 2]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.shortestAlternatingPaths(
            values[0],
            values[1],
            values[2]
        )
        assert values[3] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
