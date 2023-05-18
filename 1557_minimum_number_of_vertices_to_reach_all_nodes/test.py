from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        6,
        [[0, 1],
         [0, 2],
         [2, 5],
         [3, 4],
         [4, 2]],
        [0, 3]
    ],
    '2: leetcode example 2': [
        5,
        [[0, 1],
         [2, 1],
         [3, 1],
         [1, 4],
         [2, 4]],
        [0, 2, 3]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.findSmallestSetOfVertices(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
