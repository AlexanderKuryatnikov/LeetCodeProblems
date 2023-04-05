from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [-1, 0, 3, 5, 9, 12],
        9,
        4
    ],
    '2: leetcode example 2': [
        [-1, 0, 3, 5, 9, 12],
        2,
        -1
    ],
    '3: two elems with target 1': [
        [0, 2],
        0,
        0
    ],
    '4: two elems with target 2': [
        [0, 2],
        2,
        1
    ],
    '5: two elems without target 1': [
        [0, 2],
        -1,
        -1
    ],
    '6: two elems without target 2': [
        [0, 2],
        1,
        -1
    ],
    '5: two elems without target 3': [
        [0, 2],
        3,
        -1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.search(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
