from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[2],
         [3, 4],
         [6, 5, 7],
         [4, 1, 8, 3]],
        11
    ],
    '2: leetcode example 2': [
        [[-10]],
        -10
    ],
    '3: min through bigger number': [
        [[1],
         [1, 2],
         [1, 3, 2],
         [8, 7, 6, 5]],
        10
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minimumTotal(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
