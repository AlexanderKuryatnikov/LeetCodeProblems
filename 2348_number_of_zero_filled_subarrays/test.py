from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: 1 zero': [
        [0],
        1
    ],
    '2: 4 zeroes': [
        [0, 0, 0, 0],
        10
    ],
    '3: 2 intervals inside': [
        [1, 3, 0, 0, 2, 0, 0, 4],
        6
    ],
    '4: 2 intervals at both ends': [
        [0, 0, 0, 2, 0, 0],
        9
    ],
    '5: no zeroes': [
        [1, 2, 3],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.zeroFilledSubarray(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
