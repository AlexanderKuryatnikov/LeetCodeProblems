from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[1, 2, 3],
         [0, 2],
         [0, 1, 3],
         [0, 2]],
        False
    ],
    '2: leetcode example 2': [
        [[1, 3],
         [0, 2],
         [1, 3],
         [0, 2]],
        True
    ],
    '3: star shape': [
        [[1, 2, 3, 4],
         [0],
         [0],
         [0],
         [0]],
        True
    ],
    '4: isolated node': [
        [[],
         [2],
         [1]],
        True
    ],
    '5: isolated nodes only': [
        [[],
         [],
         []],
        True
    ],
    '6: pairs of nodes': [
        [[1],
         [0],
         [3],
         [2]],
        True
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.isBipartite(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
