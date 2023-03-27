from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]],
        7
    ],
    '2: leetcode example 2': [
        [[1, 2, 3],
         [4, 5, 6]],
        12
    ],
    '3: 1x1 grid': [
        [[1]],
        1
    ],
    '4: one row': [
        [[1, 2, 3, 4]],
        10
    ],
    '5: one column': [
        [[3], [4], [5], [6], [7]],
        25
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minPathSum(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
