from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        6
    ],
    '2: leetcode example 2': [
        [4, 2, 0, 3, 2, 5],
        9
    ],
    '3: highest in the left': [
        [4, 1, 0, 2, 0, 1],
        4
    ],
    '4: equal heights': [
        [2, 0, 0, 2, 0, 0, 2, 0, 0, 2],
        12
    ],
    '5: no trapped water': [
        [0, 2, 5, 6, 7, 5, 4, 2],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.trap(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
