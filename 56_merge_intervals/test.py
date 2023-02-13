from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: one interval': [
        [[0, 1]],
        [[0, 1]]
    ],
    '2: no everlapping intervals': [
        [[0, 1], [2, 2], [3, 5]],
        [[0, 1], [2, 2], [3, 5]]
    ],
    '3: common endpoints': [
        [[0, 1], [1, 2], [3, 5]],
        [[0, 2], [3, 5]]
    ],
    '4: intervals inside other interval': [
        [[3, 4], [0, 8], [1, 2]],
        [[0, 8]]
    ],
    '5: overlapping intervals': [
        [[8, 10], [0, 4], [7, 9], [3, 5]],
        [[0, 5], [7, 10]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.merge(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
