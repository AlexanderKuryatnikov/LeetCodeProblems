from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: one element': [
        [0],
        [[], [0]]
    ],
    '2: unique elements': [
        [1, 2, 3],
        [[],
         [1], [2], [3],
         [1, 2], [1, 3], [2, 3],
         [1, 2, 3]]
    ],
    '3: one duplicate': [
        [1, 2, 2],
        [[],
         [1], [2],
         [1, 2], [2, 2],
         [1, 2, 2]]
    ],
    '4: two duplicates': [
        [1, 2, 2, 1],
        [[],
         [1], [2],
         [1, 1], [1, 2], [2, 2],
         [1, 1, 2], [1, 2, 2],
         [1, 1, 2, 2]]
    ],
    '5: one element multiple times': [
        [1, 1, 1, 1],
        [[], [1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.subsetsWithDup(values[0])
        assert sorted(values[1]) == sorted(result), (
            f'Test {test}. Your result {result}'
        )
        print(f'Test {test}... OK')
