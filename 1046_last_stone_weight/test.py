from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example': [
        [2, 7, 4, 1, 8, 1],
        1
    ],
    '2: one stone': [
        [1],
        1
    ],
    '3: two stones with equal weight': [
        [1, 1],
        0
    ],
    '4: three stones with equal weight': [
        [5, 5, 5],
        5
    ],
    '5: leftover stone and last stone with equal weight': [
        [6, 2, 8],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.lastStoneWeight(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
