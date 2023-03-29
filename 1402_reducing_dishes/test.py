from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [-1, -8, 0, 5, -9],
        14
    ],
    '2: leetcode example 2': [
        [4, 3, 2],
        20
    ],
    '3: leetcode example 3': [
        [-1, -4, -5],
        0
    ],
    '4: one positive order': [
        [5],
        5
    ],
    '5: one negative order': [
        [-5],
        0
    ],
    '6: 1 and -1': [
        [-1, -1, -1, 1, 1],
        4
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.maxSatisfaction(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
