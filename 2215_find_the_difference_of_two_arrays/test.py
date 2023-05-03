from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 3],
        [2, 4, 6],
        [[1, 3],
         [4, 6]]
    ],
    '2: leetcode example 2': [
        [1, 2, 3, 3],
        [1, 1, 2, 2],
        [[3],
         []]
    ],
    '3: same elements': [
        [1, 1, 1, 2, 2, 3],
        [1, 2, 2, 3, 3, 3],
        [[],
         []]
    ],
    '4: no common elements': [
        [1, 2, 3],
        [4, 5, 6],
        [[1, 2, 3],
         [4, 5, 6]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.findDifference(values[0], values[1])
        result[0].sort()
        result[1].sort()
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
