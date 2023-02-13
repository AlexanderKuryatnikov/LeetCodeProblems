from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: first odd, second odd': [
        3,
        7,
        3
    ],
    '2: first even, second even': [
        8,
        10,
        1
    ],
    '3: first odd, second even': [
        3,
        10,
        4
    ],
    '4: first even, second odd': [
        4,
        7,
        2
    ],
    '5: one odd number': [
        51,
        51,
        1
    ],
    '6: one even number': [
        50,
        50,
        0
    ],
    '7: neighbouring numbers': [
        0,
        1,
        1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.countOdds(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
