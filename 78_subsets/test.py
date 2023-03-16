from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: three elements': [
        [1, 2, 3],
        [[],
         [1], [2], [3],
         [1, 2], [1, 3], [2, 3],
         [1, 2, 3]]
    ],
    '2: one element': [
        [0],
        [[], [0]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.subsets(values[0])
        assert sorted(values[1]) == sorted(result), (
            f'Test {test}. Your result {result}'
        )
        print(f'Test {test}... OK')
