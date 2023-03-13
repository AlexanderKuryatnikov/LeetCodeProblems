from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[1, 3], [3, 3], [5, 3], [2, 2]],
        [[2, 3, 1], [4, 3, 1], [1, 1, 2]],
        [3, 2, 2]
    ],
    '2: leetcode example 2': [
        [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
        [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]],
        [2, 3, 2, 4]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.countPoints(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
