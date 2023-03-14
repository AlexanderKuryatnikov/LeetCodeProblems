from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[10, 6, 9, 1],
         [7, 5, 11, 2],
         [4, 8, 3, 15]],
        2,
        [[7, 5, 11, 2],
         [10, 6, 9, 1],
         [4, 8, 3, 15]]
    ],
    '2: leetcode example 2': [
        [[3, 4],
         [5, 6]],
        0,
        [[5, 6],
         [3, 4]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.sortTheStudents(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
