from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        4,
        [[1, 2, 9],
         [2, 3, 6],
         [2, 4, 5],
         [1, 4, 7]],
        5
    ],
    '2: leetcode example 2': [
        4,
        [[1, 2, 2],
         [1, 3, 4],
         [3, 4, 7]],
        2
    ],
    '3: shortest road is unavailable': [
        4,
        [[1, 4, 10],
         [2, 3, 5]],
        10
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minScore(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
