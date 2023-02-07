from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [3, 2, 2, 3],
        3,
        2
    ],
    '2: leetcode example 2': [
        [0, 1, 2, 2, 3, 0, 4, 2],
        2,
        5
    ],
    '3: single val in the end': [
        [0, 1, 2, 3],
        3,
        3
    ],
    '4: single val in the center': [
        [0, 1, 3, 2, 7, 8],
        3,
        5
    ],
    '5: empty list': [
        [],
        3,
        0
    ],
    '6: no target in the list': [
        [1, 6, 2, 3],
        10,
        4
    ],
    '7: list of targets': [
        [1, 1, 1, 1, 1],
        1,
        0
    ],
    '8: list begins with targets': [
        [2, 2, 3],
        2,
        1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.removeElement(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
